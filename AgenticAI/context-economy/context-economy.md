# Context Economy for Agents

Context economy is the design discipline that decides what earns space in an agent's active context, what stays retrievable, what gets compressed, and what must remain auditable outside the prompt.

## Core thesis

The wrong question is "how large is the context window?"

The better questions are:
- what does this turn actually need to see?
- which tool schemas are plausible enough to promote from summary to full JSON?
- what repository context should be retrieved semantically instead of pasted wholesale?
- what memory should preserve event structure rather than flattening into facts?
- how much KV cache, latency, and cost does each added artifact impose on every future step?
- what should be kept outside the model context for audit, replay, or privacy reasons?

Agent systems that skip those questions will waste tokens, degrade reasoning, and confuse context abundance with operational durability.

## Why this topic now

The 2026-04-24 scan produced three reinforcing signals:

1. **DeepSeek-V4** makes long-context agent work a KV-cache and serving-efficiency problem. A 1M-token window matters only if every continuation at that depth remains affordable.
2. **Tool Attention** names the MCP/tools tax and proposes dynamic tool gating plus lazy schema loading instead of eagerly injecting every tool schema.
3. **Claude Context** is the GitHub-trending practical version for code agents: index the repository and retrieve relevant code into the agent context instead of loading everything.
4. **StructMem** extends the same lesson to memory: not every remembered item should be a flat fact; some context needs event structure and cross-event links.

Core sources:
- DeepSeek-V4 on Hugging Face: https://huggingface.co/blog/deepseekv4
- Tool Attention: https://arxiv.org/abs/2604.21816
- Claude Context: https://github.com/zilliztech/claude-context
- StructMem: https://arxiv.org/abs/2604.21748
- LightMem: https://github.com/zjunlp/LightMem

## The context budget is multi-dimensional

Token count is only the visible cost. Real agent context has at least six budgets:

### 1. Token budget
Every tool schema, file snippet, memory, and prior turn competes for prompt space.

### 2. KV-cache budget
Long-running sessions pay for retained context again and again during decoding. KV-cache growth is an infrastructure cost, not just a model limit.

### 3. Latency budget
Agents amplify latency because a single task can contain many model calls, tool calls, retries, approvals, and handoffs.

### 4. Reasoning budget
Irrelevant context can degrade decisions even when the model technically fits the window.

### 5. Governance budget
The model should not see tools, data, or memories that violate access scope just because they were available in a server registry.

### 6. Audit budget
Some evidence should stay outside the active prompt but remain replayable and inspectable later.

## What to build now

### Gate tools before schema injection
Keep compact tool summaries in context. Promote full schemas only when intent, state, and permissions make the tool plausible.

Minimum pattern:
1. maintain a tool registry with short summaries, preconditions, and scopes
2. embed summaries for rough intent matching
3. filter candidates with current state and access policy
4. load full schemas only for top-k tools
5. log when a needed tool was gated out so the router can improve

### Retrieve code context semantically
Large repositories should be searchable context stores, not prompt dumps. Use repository indexing, symbol search, exact file reads, and citations back to source files.

Practical starting points:
- `zilliztech/claude-context`
- local embeddings plus pgvector, Milvus, Zilliz, LanceDB, or SQLite vector extensions
- language-server symbol search paired with semantic search

### Measure context cost per agent loop
For every serious run, record:
- prompt tokens by category: user, memory, tools, retrieved code, previous turns
- number and size of injected tool schemas
- context length at each model call
- KV-cache or serving-memory pressure where available
- latency by model call, tool call, and router decision

If those numbers are invisible, context bloat will look like model weakness.

### Keep memory structured when continuity depends on it
Memory that supports long-horizon behavior should preserve event identity, timestamps, provenance, relationships, and supersession. Flat summaries are fine for some personalization facts; they are not enough for temporal reasoning or audit.

## What to avoid

Avoid these traps:
- treating a million-token window as permission to stop selecting context
- injecting every MCP schema on every turn
- loading whole repositories into prompts instead of indexing them
- using vector search as the only memory architecture
- hiding context growth inside framework internals with no telemetry
- allowing tool visibility to bypass access policy
- optimizing benchmark prompts while production sessions drown in tool and memory payloads

## Practical tools and methods worth exploring now

- [DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) for long-context open-model experiments
- [Tool Attention](https://arxiv.org/abs/2604.21816) for dynamic tool gating patterns
- [Claude Context](https://github.com/zilliztech/claude-context) for code-search MCP integration
- [LightMem](https://github.com/zjunlp/LightMem) for memory-augmented generation patterns
- vLLM or SGLang serving metrics for long-context and multi-agent tests
- OpenTelemetry-style agent traces with prompt-category token breakdowns

## Working conclusion

The future agent stack is not context maximalism. It is context accounting. Systems that know what to admit, retrieve, compress, cache, and audit will beat systems that merely buy larger windows and hope the model sorts it out.

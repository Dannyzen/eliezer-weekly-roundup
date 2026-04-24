# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-24

### DeepSeek-V4 makes long-context agent work a KV-cache problem
Summary: DeepSeek-V4 is a long-context open model release shaped around agent workloads: compressed attention, smaller KV caches, reasoning continuity across tool-bearing turns, typed tool-call schema, and sandbox-backed RL rollouts.

Analysis: [reasoning analysis](2026-04-24/reasoning.md#deepseek-v4-makes-long-context-agent-work-a-kv-cache-problem)
Durable topic: [Context Economy for Agents](context-economy/context-economy.md)
Core source: [DeepSeek-V4: a million-token context that agents can actually use](https://huggingface.co/blog/deepseekv4)
Supporting sources:
- [DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)
Implementable now:
- test the Flash checkpoint before assuming the larger Pro model is operationally practical
- measure KV-cache growth and per-turn latency in long-running agent sessions
- design typed tool-call envelopes that avoid JSON-in-string escaping failures
- treat sandbox replay and preemption recovery as agent-training infrastructure
Tools, repos, and methodologies worth exploring:
- DeepSeek-V4 checkpoints on Hugging Face
- KV-cache telemetry for agent loops
- XML or typed tool-call payloads
- replayable sandbox rollouts for RL and evaluation
Implementability score: 0.62

### Tool and code context should be gated, not eagerly injected
Summary: MCP tool inventories and large codebases should be admitted into context selectively. Tool Attention gives the lazy-schema-loading pattern; `claude-context` is the practical GitHub-trending code-search MCP to try now.

Analysis: [reasoning analysis](2026-04-24/reasoning.md#tool-and-code-context-should-be-gated-not-eagerly-injected)
Durable topic: [Context Economy for Agents](context-economy/context-economy.md)
Core source: [Tool Attention Is All You Need](https://arxiv.org/abs/2604.21816)
Supporting source: [zilliztech/claude-context](https://github.com/zilliztech/claude-context)
Implementable now:
- keep compact tool summaries in prompt context and lazily load full schemas for top-k candidates
- filter tools by intent, state preconditions, and access scope before model exposure
- use semantic code-search MCPs instead of loading whole repositories into prompts
- track per-turn tool-schema tokens as a runtime metric
Tools, repos, and methodologies worth exploring:
- [Tool Attention](https://arxiv.org/abs/2604.21816)
- [zilliztech/claude-context](https://github.com/zilliztech/claude-context)
- MCP summary registries
- lazy JSON-schema loading
- Milvus, Zilliz, pgvector, or local vector search for code context
Implementability score: 0.82

### StructMem argues agent memory needs event structure, not just facts
Summary: Long-term agent memory has to preserve event bindings, temporal anchors, and cross-event relationships. Flat vectorized facts are too weak for temporal reasoning and multi-hop continuity.

Analysis: [reasoning analysis](2026-04-24/reasoning.md#structmem-argues-agent-memory-needs-event-structure-not-just-facts)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [StructMem: Structured Memory for Long-Horizon Behavior in LLMs](https://arxiv.org/abs/2604.21748)
Supporting source: [zjunlp/LightMem](https://github.com/zjunlp/LightMem)
Implementable now:
- store memory as events with IDs, timestamps, provenance, and relationship candidates
- run background consolidation to link, merge, or supersede memories
- retrieve event neighborhoods instead of isolated chunks
- evaluate with temporal and multi-hop memory questions
Tools, repos, and methodologies worth exploring:
- [StructMem](https://arxiv.org/abs/2604.21748)
- [zjunlp/LightMem](https://github.com/zjunlp/LightMem)
- LoCoMo-style temporal memory evals
- background consolidation jobs
- event-neighborhood retrieval
Implementability score: 0.69

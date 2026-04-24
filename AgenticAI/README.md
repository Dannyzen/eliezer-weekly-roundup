# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-24

### Context admission control is now the main agent runtime job
Summary: The week’s strongest agent-stack pattern is not “bigger context.” It is deciding what earns active context: tool schemas, repository snippets, memory neighborhoods, reasoning traces, and KV cache all need explicit budgets.

Analysis: [reasoning analysis](2026-04-24/reasoning.md#context-admission-control-is-now-the-main-agent-runtime-job)
Durable topic: [Context Economy for Agents](context-economy/context-economy.md)
Core source: [Tool Attention Is All You Need](https://arxiv.org/abs/2604.21816)
Supporting sources:
- [DeepSeek-V4: a million-token context that agents can actually use](https://huggingface.co/blog/deepseekv4)
- [zilliztech/claude-context](https://github.com/zilliztech/claude-context)
- [StructMem](https://arxiv.org/abs/2604.21748)
Implementable now:
- keep compact tool summaries in prompt context and lazily load full schemas only for top-k candidates
- use semantic code-search MCPs instead of loading entire repositories into prompts
- measure prompt tokens by category: tools, memory, retrieved code, prior turns, and user input
- track context length, KV-cache pressure, and per-turn latency in long-running agent sessions
Tools, repos, and methodologies worth exploring:
- Tool Attention-style lazy schema loading
- `zilliztech/claude-context`
- DeepSeek-V4-Flash for long-context agent experiments
- OpenTelemetry-style agent traces with token-category breakdowns
Implementability score: 0.84

### Agent harnesses are becoming sessionful products, not throwaway prompts
Summary: OpenAI workspace agents, WebSocket-based Responses API flows, AG2’s v1.0 cleanup path, and the agent-harness design literature all point in the same direction: agents are becoming durable, observable sessions with tool mediation and resumable state.

Analysis: [reasoning analysis](2026-04-24/reasoning.md#agent-harnesses-are-becoming-sessionful-products-not-throwaway-prompts)
Durable topic: [Sessionful Agent Loops](sessionful-agent-loops/sessionful-agent-loops.md)
Core source: [Introducing workspace agents in ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt)
Supporting sources:
- [Speeding up agentic workflows with WebSockets in the Responses API](https://openai.com/index/speeding-up-agentic-workflows-with-websockets)
- [Architectural Design Decisions in AI Agent Harnesses](https://arxiv.org/abs/2604.18071v1)
- [AG2 v0.12.0](https://github.com/ag2ai/ag2/releases/tag/v0.12.0)
Implementable now:
- separate the agent harness from the prompt: state, tool mediation, approval, retry, and compaction are runtime concerns
- make long-running sessions resumable and inspectable
- instrument model calls, tool calls, retries, and human approvals as one trace
- treat WebSocket or streaming transport as an agent latency primitive, not a UI flourish
Tools, repos, and methodologies worth exploring:
- AG2, Pydantic AI, LangGraph, Temporal, OpenTelemetry
- session state stores with checkpoint/replay semantics
- Responses API WebSocket-style persistent connections
- architecture decision records for agent harnesses
Implementability score: 0.88

### Environment-first evaluation is becoming the agent reliability substrate
Summary: The week’s eval work points away from static leaderboard prompts and toward verifiable or generated environments, repeatability tests, and trajectory-level diagnosis. For agents, success once is not reliability.

Analysis: [reasoning analysis](2026-04-24/reasoning.md#environment-first-evaluation-is-becoming-the-agent-reliability-substrate)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [Ecom-RLVE: Adaptive Verifiable Environments for E-Commerce Conversational Agents](https://huggingface.co/blog/ecom-rlve)
Supporting sources:
- [On the Reliability of Computer Use Agents](https://arxiv.org/abs/2604.17849)
- [ClawEnvKit](https://arxiv.org/abs/2604.18543v1)
- [OpenMobile](https://arxiv.org/abs/2604.15093)
- [ATBench-Claw and ATBench-CodeX](https://arxiv.org/abs/2604.14858)
Implementable now:
- build task environments with explicit success checkers instead of relying on judge-model vibes
- rerun the same task multiple times and record success variance, not just best-case success
- preserve trajectories for diagnosis: observation, action, tool output, policy check, and final state
- generate environment variants to prevent benchmark overfitting
Tools, repos, and methodologies worth exploring:
- `owlgebra-ai/EcomRLVE-Gym`
- generated environment pipelines such as ClawEnvKit
- repeated-run reliability suites for browser, desktop, and code agents
- trajectory safety benchmarks and replay harnesses
Implementability score: 0.86

### Memory is becoming a compression and reconciliation lifecycle
Summary: Memory work this week converged on one idea: agent memory is not a vector store. It is a lifecycle that preserves evidence, compresses experience into skills or rules, reconciles writes, and retrieves structured event neighborhoods when temporal reasoning matters.

Analysis: [reasoning analysis](2026-04-24/reasoning.md#memory-is-becoming-a-compression-and-reconciliation-lifecycle)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [StructMem: Structured Memory for Long-Horizon Behavior in LLMs](https://arxiv.org/abs/2604.21748)
Supporting sources:
- [Experience Compression Spectrum](https://arxiv.org/abs/2604.15877)
- [WorldDB](https://arxiv.org/abs/2604.18478v1)
- [zjunlp/LightMem](https://github.com/zjunlp/LightMem)
Implementable now:
- store memory as events with IDs, timestamps, provenance, participants, and relation candidates
- run background consolidation to merge, link, supersede, or promote memories
- retrieve event neighborhoods rather than isolated nearest-neighbor chunks
- separate episodic evidence, procedural skills, and compact rules
Tools, repos, and methodologies worth exploring:
- LightMem
- LoCoMo-style temporal memory evaluations
- background memory consolidation jobs
- write-time reconciliation policies for supersession and contradiction
Implementability score: 0.72

### Runtime compaction and local structured output are now boring plumbing
Summary: Pydantic AI’s release cadence this week shows agent frameworks converging on practical runtime primitives: stateful compaction, local structured output, tool-call retries, OpenTelemetry spans, and safer provider adapters.

Analysis: [reasoning analysis](2026-04-24/reasoning.md#runtime-compaction-and-local-structured-output-are-now-boring-plumbing)
Core source: [Pydantic AI v1.84.0](https://github.com/pydantic/pydantic-ai/releases/tag/v1.84.0)
Supporting source: [Pydantic AI v1.86.1](https://github.com/pydantic/pydantic-ai/releases/tag/v1.86.1)
Implementable now:
- add stateful compaction before long sessions collapse under transcript growth
- use local structured-output paths where Ollama or local models are adequate
- preserve validation errors and retries as traceable tool-call events
- emit tool-execution spans so observability covers the agent runtime, not only model latency
Tools, repos, and methodologies worth exploring:
- Pydantic AI
- OpenAI response compaction patterns
- Ollama structured output paths
- OpenTelemetry `gen_ai.operation.name=execute_tool` spans
Implementability score: 0.95

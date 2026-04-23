# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-23

### Sessionful agent loops are becoming the real agent product surface
Summary: Shared cloud agents, persistent workspaces, approvals, analytics, and connection-scoped transport caches all point to the same shift: serious agent systems are moving from stateless chat wrappers to bounded long-lived runs.

Analysis: [reasoning analysis](2026-04-23/reasoning.md#sessionful-agent-loops-are-becoming-the-real-agent-product-surface)
Durable topic: [Sessionful Agent Loops](sessionful-agent-loops/sessionful-agent-loops.md)
Core source: [Introducing workspace agents in ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt)
Supporting sources:
- [Speeding up agentic workflows with WebSockets in the Responses API](https://openai.com/index/speeding-up-agentic-workflows-with-websockets)
- [Workspace agents](https://openai.com/academy/workspace-agents)
Implementable now:
- keep long-running work inside explicit run or session objects instead of rebuilding full state every turn
- cache validated context and reusable transport state across tool calls
- add approval checkpoints for side-effectful actions before they execute
- compare product and open-source harnesses on the same session, memory, and governance dimensions
Tools, repos, and methodologies worth exploring:
- [OpenAI workspace agents](https://openai.com/index/introducing-workspace-agents-in-chatgpt)
- [Responses API WebSockets](https://openai.com/index/speeding-up-agentic-workflows-with-websockets)
- `previous_response_id` state reuse
- connection-scoped caches
- [huggingface/ml-intern](https://github.com/huggingface/ml-intern)
Implementability score: 0.93

### SWE-chat shows benchmark realism now depends on wild interaction traces
Summary: Real coding-agent traces show what curated benchmarks miss: interruption, correction, code survival, and security quality inside human-agent collaboration.

Analysis: [reasoning analysis](2026-04-23/reasoning.md#swe-chat-shows-benchmark-realism-now-depends-on-wild-interaction-traces)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [SWE-chat: Coding Agent Interactions From Real Users in the Wild](https://arxiv.org/abs/2604.20779)
Implementable now:
- measure how much agent-produced code survives into committed diffs
- log interruptions, rewrites, and correction turns as first-class eval events
- compare security quality on agent-authored versus human-authored code
- treat real-user trace collection as core evaluation infrastructure
Tools, repos, and methodologies worth exploring:
- [SWE-chat](https://arxiv.org/abs/2604.20779)
- trace-first coding-agent dashboards
- commit-level authorship and code-survival analysis
- security scans segmented by code authorship
- [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Implementability score: 0.74

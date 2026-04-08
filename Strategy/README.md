# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-08

### Microsoft Agent Framework 1.0 shows framework competition moving toward governed workflow substrates
Summary: The signal is not just another SDK launch. A major vendor is treating checkpoints, graph orchestration, observability, and migration paths as baseline requirements for real agent systems.

Analysis: [sovereignty analysis](2026-04-08/sovereignty.md#microsoft-agent-framework-10-shows-framework-competition-moving-toward-governed-workflow-substrates)
Core source: [microsoft/agent-framework](https://github.com/microsoft/agent-framework)
Implementable now:
- adopt graph workflows with checkpoints instead of opaque chat loops
- wire agent traces into OpenTelemetry so platform teams can inspect them with normal tooling
- add middleware layers for approvals, policy injection, and exception handling
- compare existing AutoGen or Semantic Kernel flows against more explicit workflow graphs
Implementability score: 0.93

### Back-Reveal shows why memory and retrieval tools cannot share a trust boundary with the agent brain
Summary: Tool access is now a security boundary. If the same agent loop can read durable memory and make outbound calls, one backdoor can turn memory into an exfiltration channel.

Analysis: [sovereignty analysis](2026-04-08/sovereignty.md#back-reveal-shows-why-memory-and-retrieval-tools-cannot-share-a-trust-boundary-with-the-agent-brain)
Core source: [Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use](https://arxiv.org/abs/2604.05432)
Implementable now:
- separate read-memory permissions from outbound retrieval or network permissions
- inspect tool-call arguments before execution
- keep durable memory behind narrow interfaces instead of broad tool access
- alert on suspicious memory-read plus outbound-call patterns across a session
Implementability score: 0.67

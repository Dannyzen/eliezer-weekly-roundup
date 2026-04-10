# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-10

### Governed workflow substrates are becoming the enterprise default
Summary: The strategic winner this week was the governed runtime substrate: checkpoints, approvals, traces, and policy hooks are becoming the actual enterprise product surface for agents.

Analysis: [sovereignty analysis](2026-04-10/sovereignty.md#governed-workflow-substrates-are-becoming-the-enterprise-default)
Durable topic: [Governed Workflow Substrates](governed-workflow-substrates/governed-workflow-substrates.md)
Core source: [microsoft/agent-framework](https://github.com/microsoft/agent-framework)
Implementable now:
- make checkpoints, approvals, and audit logs default architecture
- compare frameworks on policy hooks and replayability, not prompt ergonomics
- require intervention paths for critical workflows
- attach policy engines to runtime events
Tools, repos, and methodologies worth exploring:
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- Agent Governance Toolkit
- workflow replay logs
- approval middleware
- runtime policy engines
Implementability score: 0.94

### Security evaluation is moving inside the trajectory and across adaptive attacks
Summary: The market still wants to sell answer-boundary safety, but the better work now measures multi-step behavior, memory risk, and adaptive prompt-injection failure.

Analysis: [sovereignty analysis](2026-04-10/sovereignty.md#security-evaluation-is-moving-inside-the-trajectory-and-across-adaptive-attacks)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [PIArena paper](https://arxiv.org/abs/2604.08499v1)
Implementable now:
- test safety at the step and trajectory level
- run adaptive prompt-injection evaluations across multiple tasks
- separate trust boundaries between memory, retrieval, planning, and tools
- add policy mediation and retrieval isolation
Tools, repos, and methodologies worth exploring:
- adaptive red-teaming harnesses
- tool-scoped sandboxes
- trajectory-aware safety review
- retrieval isolation
- provenance and audit logging
Implementability score: 0.74

### Local-first agent infrastructure is finally credible
Summary: Gemma 4 plus LiteRT-LM made local-first multimodal agent systems feel like a real engineering option instead of a sacrifice narrative.

Analysis: [sovereignty analysis](2026-04-10/sovereignty.md#local-first-agent-infrastructure-is-finally-credible)
Durable topic: [Local-First Agents](local-first-agents/local-first-agents.md)
Core source: [Google Developers Blog: Gemma 4 on the edge](https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/)
Implementable now:
- prototype local-first copilots around bounded sensitive workflows
- route specialized overflow to cloud models only when needed
- benchmark privacy, latency, and capability tradeoffs directly
- pair local inference with owned local state storage
Tools, repos, and methodologies worth exploring:
- Gemma 4
- LiteRT-LM
- local SQLite or event-log state stores
- hybrid model routing policies
- device-local eval suites
Implementability score: 0.88

### Shared state is the missing sovereignty layer for personal agents
Summary: The user does not really own the agent stack if state is fragmented across chat history, generated apps, and opaque logs; shared artifacts plus governed write-back are the more durable model.

Analysis: [sovereignty analysis](2026-04-10/sovereignty.md#shared-state-is-the-missing-sovereignty-layer-for-personal-agents)
Durable topic: [Shared-State Agents](shared-state-agents/shared-state-agents.md)
Core source: [PSI paper](https://arxiv.org/abs/2604.08529v1)
Implementable now:
- model shared artifacts with typed schemas and ownership metadata
- expose write-back as governed capabilities
- keep audit logs for changes across interfaces
- start with a local state bus for a small set of tools
Tools, repos, and methodologies worth exploring:
- local SQLite or append-only event logs
- typed artifact registries
- pub/sub patterns for personal tool coordination
- policy checks around state mutation
- provenance logging
Implementability score: 0.57

# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-22

### Deep Dive Wednesday winner: Sandbox-native agent workers turn execution substrate into the product surface
Summary: OpenAI's Agents SDK now ships Sandbox Agents with persistent isolated workspaces, manifests, snapshots, resume support, workspace memory, and local, Docker, or hosted backends. The important shift is not one more tool call. It is that the worker runtime itself is becoming a first-class design surface.

Analysis: [reasoning analysis](2026-04-22/reasoning.md#deep-dive-wednesday-winner)
Durable topic: [Sandbox-Native Agent Workers](sandbox-native-agent-workers/sandbox-native-agent-workers.md)
Core source: [OpenAI Agents SDK v0.14.0](https://github.com/openai/openai-agents-python/releases/tag/v0.14.0)
Supporting source: [The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk)
Implementable now:
- define long-running workers through manifests instead of improvised shell sessions
- use local or Docker sandbox clients as explicit execution backends
- snapshot and resume non-trivial runs instead of forcing them into one uninterrupted session
- keep worker memory and mounts explicit so state stays inspectable
Tools, repos, and methodologies worth exploring:
- [openai/openai-agents-python](https://github.com/openai/openai-agents-python)
- [Sandbox Agents docs](https://openai.github.io/openai-agents-python/sandbox_agents/)
- `UnixLocalSandboxClient`
- `DockerSandboxClient`
- [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Implementability score: 0.95

### Delegation should be calibrated to context, not static agent roles
Summary: The same agent can be strong on short, self-contained tasks and weak on long-horizon or dependency-heavy work. Static capability profiles blur that difference and cause systematic misdelegation.

Analysis: [reasoning analysis](2026-04-22/reasoning.md#delegation-should-be-calibrated-to-context-not-static-agent-roles)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [CADMAS-CTX](https://arxiv.org/abs/2604.17950)
Implementable now:
- bucket tasks by coarse context before routing them across agents
- keep per-agent success posteriors instead of one global reputation score
- penalize delegation decisions when evidence is sparse or noisy
- log enough delegation context that routing can improve over time
Tools, repos, and methodologies worth exploring:
- [CADMAS-CTX](https://arxiv.org/abs/2604.17950)
- contextual bandit or Beta-posterior routing
- delegation event logs and per-context scorecards
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [microsoft/agent-framework](https://github.com/microsoft/agent-framework)
Implementability score: 0.79

### Repeatability is becoming the real reliability metric for computer-use agents
Summary: A computer-use agent that succeeds once and fails on the same task the next run is not reliable. Repeated execution, ambiguity handling, and behavior stability are now the meaningful evaluation surface.

Analysis: [reasoning analysis](2026-04-22/reasoning.md#repeatability-is-becoming-the-real-reliability-metric-for-computer-use-agents)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [On the Reliability of Computer Use Agents](https://arxiv.org/abs/2604.17849)
Implementable now:
- rerun browser or desktop tasks multiple times before trusting pass rates
- track ambiguity and clarification failure as first-class error modes
- separate stochastic flukes from stable behaviors in benchmark reporting
- favor strategies that stay within a narrow behavioral envelope across runs
Tools, repos, and methodologies worth exploring:
- [On the Reliability of Computer Use Agents](https://arxiv.org/abs/2604.17849)
- repeated-run evaluation harnesses
- replayable browser or desktop task environments
- OpenTelemetry-style trace capture
- stability dashboards that compare runs of the same task
Implementability score: 0.86

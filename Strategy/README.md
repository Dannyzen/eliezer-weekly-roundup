# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-22

### Local-first claims need task-shaped benchmarking, not slogans
Summary: Structured extraction workloads are much closer to local-ready than long-context coaching or correction work. Local-first is becoming a routing policy, not a purity test.

Analysis: [sovereignty analysis](2026-04-22/sovereignty.md#local-first-claims-need-task-shaped-benchmarking-not-slogans)
Durable topic: [Local-First Agents](local-first-agents/local-first-agents.md)
Core source: [Benchmarking System Dynamics AI Assistants](https://arxiv.org/abs/2604.18566)
Implementable now:
- benchmark each subtask separately before choosing a local or cloud default
- route structured extraction and schema-constrained work to local models first
- escalate long-context correction or coaching tasks selectively to cloud
- test backend behavior and JSON guarantees before spending effort on quantization sweeps
Tools, repos, and methodologies worth exploring:
- [Benchmarking System Dynamics AI Assistants](https://arxiv.org/abs/2604.18566)
- [llama.cpp](https://github.com/ggml-org/llama.cpp)
- [mlx-lm](https://github.com/ml-explore/mlx-lm)
- task-specific local-versus-cloud routing tables
- backend-specific JSON conformance tests
Implementability score: 0.90

### High-autonomy security agents are forcing containment into the product surface
Summary: If an agent can inspect source and execute real exploits, containment is part of the product. Read-only mounts, writable overlays, and self-hosted runner boundaries are becoming default design expectations.

Analysis: [sovereignty analysis](2026-04-22/sovereignty.md#high-autonomy-security-agents-are-forcing-containment-into-the-product-surface)
Durable topic: [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md)
Core source: [Shannon v1.1.0](https://github.com/KeygraphHQ/shannon/releases/tag/v1.1.0)
Supporting source: [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)
Implementable now:
- run exploit-capable agents only on staging or disposable environments
- mount source read-only and give the agent a separate writable overlay
- keep exploit candidate queues structured and inspectable
- prefer self-hosted runner models when the agent touches proprietary code or live-like systems
Tools, repos, and methodologies worth exploring:
- [Shannon v1.1.0](https://github.com/KeygraphHQ/shannon/releases/tag/v1.1.0)
- [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)
- read-only mounts plus writable overlays
- self-hosted runner deployments
- proof-producing exploit queues and replayable reports
Implementability score: 0.92

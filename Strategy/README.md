# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-10

### PIArena turns prompt injection defense into a real comparative evaluation problem
Summary: The important result is not that prompt injection is dangerous. We knew that. The useful result is that cross-benchmark and adaptive-attack evaluation now makes weak defenses much harder to hide behind marketing.

Analysis: [sovereignty analysis](2026-04-10/sovereignty.md#piarena-turns-prompt-injection-defense-into-a-real-comparative-evaluation-problem)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [PIArena paper](https://arxiv.org/abs/2604.08499v1)
Implementable now:
- test injection defenses across multiple task families and content channels
- include adaptive attacks that react to defense behavior
- combine prompt-layer defenses with tool scoping and policy mediation
- separate defense generalization scores from single-benchmark win rates
Tools, repos, and methodologies worth exploring:
- attack/defense benchmark matrices
- retrieval isolation for untrusted content
- runtime policy mediation in front of tools
- adaptive prompt-injection red-teaming
Implementability score: 0.76

### PSI argues that shared state is the missing sovereignty layer for personal agents
Summary: Local-first branding is not enough. The strategic shift comes when the user owns a durable shared state layer that tools and chat can both operate on without collapsing into transcript soup.

Analysis: [sovereignty analysis](2026-04-10/sovereignty.md#psi-argues-that-shared-state-is-the-missing-sovereignty-layer-for-personal-agents)
Durable topic: [Shared-State Agents](shared-state-agents/shared-state-agents.md)
Core source: [PSI paper](https://arxiv.org/abs/2604.08529v1)
Implementable now:
- introduce a local state bus for generated tools and assistants
- model shared artifacts with typed schemas and ownership metadata
- expose write-back as governed capabilities
- treat chat as a view over shared state rather than the state store itself
Tools, repos, and methodologies worth exploring:
- local SQLite or event-log-backed state stores
- pub/sub patterns for personal tool coordination
- typed artifact registries
- audit logs for write-back actions across interfaces
Implementability score: 0.57

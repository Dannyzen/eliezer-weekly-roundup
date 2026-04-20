# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-20

### Experience compression is becoming the right mental model for agent memory
Summary: Memory, skills, and rules are not separate features. They are compression levels on the same experience pipeline, and most current systems still cannot move knowledge adaptively across those levels.

Analysis: [reasoning analysis](2026-04-20/reasoning.md#experience-compression-is-becoming-the-right-mental-model-for-agent-memory)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [Experience Compression Spectrum](https://arxiv.org/abs/2604.15877)
Implementable now:
- separate stored experience into episodes, reusable routines, and compact rules
- promote memories upward in background jobs instead of forcing every recall through transcript search
- choose retrieval depth by query risk, time horizon, and privacy tier
- measure transfer gain, token savings, and reversibility together
Tools, repos, and methodologies worth exploring:
- [Experience Compression Spectrum](https://arxiv.org/abs/2604.15877)
- background consolidation loops for memory promotion
- skill distillation pipelines
- rule extraction from repeated trajectories
- tiered memory objects with explicit promotion criteria
Implementability score: 0.74

### Multi-agent reliability improves faster when you subsidize the weak link
Summary: Many multi-agent systems are bottlenecked by one flaky role. Reliability improves faster when you locate that weak link and allocate more reasoning budget there instead of scaling every role evenly.

Analysis: [reasoning analysis](2026-04-20/reasoning.md#multi-agent-reliability-improves-faster-when-you-subsidize-the-weak-link)
Core source: [Weak-Link Optimization for Multi-Agent Reasoning and Collaboration](https://arxiv.org/abs/2604.15972)
Implementable now:
- score each agent role for reliability instead of hiding instability in one system average
- route extra sampling or review budget to the weakest role first
- add per-role instability dashboards to multi-agent evals
- make weak-link localization a standard pre-optimization step
Tools, repos, and methodologies worth exploring:
- [Weak-Link Optimization for Multi-Agent Reasoning and Collaboration](https://arxiv.org/abs/2604.15972)
- per-role reliability scoring
- uncertainty-driven budget allocation
- repeated sampling only on unstable roles
- multi-agent failure propagation analysis
Implementability score: 0.83

### Runtime compaction and local structured output are becoming the same product surface
Summary: Serious agent runtimes are making context compaction and local structured tool use explicit configuration surfaces instead of hoping long runs and local providers behave like hosted defaults.

Analysis: [reasoning analysis](2026-04-20/reasoning.md#runtime-compaction-and-local-structured-output-are-becoming-the-same-product-surface)
Core source: [PydanticAI v1.84.0](https://github.com/pydantic/pydantic-ai/releases/tag/v1.84.0)
Implementable now:
- enable compaction on long-running sessions before context blowups appear in production
- regression-test structured outputs on local or OpenAI-compatible providers
- treat compaction policy and schema fidelity as part of the runtime contract
- standardize local structured tool use around explicit capability tests
Tools, repos, and methodologies worth exploring:
- [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)
- [PydanticAI v1.84.0](https://github.com/pydantic/pydantic-ai/releases/tag/v1.84.0)
- [Ollama](https://ollama.com)
- structured output regression tests
- compaction policy configuration and replay tests
Implementability score: 0.95

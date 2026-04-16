# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-16

### Cross-domain memory transfer works when memories become reusable guidance
Summary: The best new memory signal is not bigger storage. It is better promotion. Memory Transfer Learning shows that coding agents benefit when they retrieve abstract insights and validation routines across task domains instead of replaying raw traces.

Analysis: [reasoning analysis](2026-04-16/reasoning.md#cross-domain-memory-transfer-works-when-memories-become-reusable-guidance)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [Memory Transfer Learning](https://arxiv.org/abs/2604.14004)
Implementable now:
- promote reusable validation routines and workflow guidance into durable memory
- keep raw trajectories and distilled insights in separate memory tiers
- prefer abstract cross-domain retrieval before task-specific trace injection
- score memory by transfer gain across task families
Tools, repos, and methodologies worth exploring:
- [Memory Transfer Learning project page](https://memorytransfer.github.io/)
- [MemoryTransferLearning code](https://github.com/KangsanKim07/MemoryTransferLearning)
- insight-first retrieval
- memory promotion pipelines
- cross-domain evaluation
Implementability score: 0.86

### Embeddable agent kernels beat UI-locked coding assistants
Summary: Sema Code’s strongest idea is architectural, not cosmetic. The coding agent core should be reusable infrastructure that can power IDE, CLI, and messaging clients instead of being trapped inside one shell.

Analysis: [reasoning analysis](2026-04-16/reasoning.md#embeddable-agent-kernels-beat-ui-locked-coding-assistants)
Durable topic: [Embeddable Agent Kernels](embeddable-agent-kernels/embeddable-agent-kernels.md)
Core source: [Sema Code](https://arxiv.org/abs/2604.11045)
Implementable now:
- split agent kernels from presentation surfaces
- centralize permissions, task state, and background execution in the shared core
- expose the core as a library or service with typed hooks
- keep clients thin and replaceable
Tools, repos, and methodologies worth exploring:
- [sema-code-core](https://github.com/midea-ai/sema-code-core)
- [sema-code-vscode-extension](https://github.com/midea-ai/sema-code-vscode-extension)
- kernel-plus-client design
- MCP and skills as extension surfaces
Implementability score: 0.89

### Dynamic execution benchmarks are finally measuring tool use
Summary: GeoAgentBench is useful because it measures the part most benchmarks miss: whether the agent actually operated tools correctly in a live environment, with the right parameters, recovery behavior, and output verification.

Analysis: [reasoning analysis](2026-04-16/reasoning.md#dynamic-execution-benchmarks-are-finally-measuring-tool-use)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [GeoAgentBench](https://arxiv.org/abs/2604.13888)
Implementable now:
- add parameter-level execution metrics to tool benchmarks
- verify outputs with the modality that matters
- benchmark recovery loops instead of only clean-path success
- score planning quality separately from execution quality
Tools, repos, and methodologies worth exploring:
- [GeoAgentBench paper](https://arxiv.org/abs/2604.13888)
- [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- execution-sandbox eval harnesses
- multimodal verification
- plan-versus-react scorecards
Implementability score: 0.73

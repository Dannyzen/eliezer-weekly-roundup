# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-17

### Portable procedure stacks are replacing prompt-native agent products
Summary: The strongest implementation pattern of the week is that reusable procedure is becoming the durable unit of leverage. Artifact-first workspaces, skill packs, and harnessed workflows are beating prompt-only agent sessions.

Analysis: [reasoning analysis](2026-04-17/reasoning.md#portable-procedure-stacks-are-replacing-prompt-native-agent-products)
Durable topic: [File-as-Bus Workspaces](file-as-bus-workspaces/file-as-bus-workspaces.md)
Core source: [Toward Autonomous Long-Horizon Engineering for ML Research](https://arxiv.org/abs/2604.13018)
Implementable now:
- make files, manifests, and validation artifacts the shared bus for long-running agent work
- package workflows as reusable skills or harnesses with explicit gates
- re-ground delegated agents on durable project artifacts instead of huge prompt history
- expose task and blocker state as operator-visible workflow state
Tools, repos, and methodologies worth exploring:
- [AweAI-Team/AiScientist](https://github.com/AweAI-Team/AiScientist)
- [obra/superpowers](https://github.com/obra/superpowers)
- [coleam00/Archon](https://github.com/coleam00/Archon)
- [multica-ai/multica](https://github.com/multica-ai/multica)
- artifact-first delegation
- skill-packaged workflows
Implementability score: 0.94

### Memory is becoming an explicit subsystem with promotion, compression, and transfer
Summary: The useful memory pattern is no longer “store more context.” It is “promote better lessons.” Cross-domain transfer and operator-visible memory tooling both point toward memory as an engineered subsystem.

Analysis: [reasoning analysis](2026-04-17/reasoning.md#memory-is-becoming-an-explicit-subsystem-with-promotion-compression-and-transfer)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [Memory Transfer Learning](https://arxiv.org/abs/2604.14004)
Implementable now:
- promote validation routines and debugging heuristics into first-class memory objects
- keep compressed insights and raw traces in different tiers
- require citations or provenance on recalled memories
- measure transfer gain across task families
Tools, repos, and methodologies worth exploring:
- [MemoryTransferLearning code](https://github.com/KangsanKim07/MemoryTransferLearning)
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
- [Dual-trace memory paper](https://arxiv.org/abs/2604.12948)
- insight-first retrieval
- memory promotion pipelines
Implementability score: 0.91

### Execution-first evaluation is replacing answer-only benchmarking
Summary: Benchmarks are finally becoming useful when they watch tool execution, parameter quality, recovery loops, and output verification instead of only grading the final answer.

Analysis: [reasoning analysis](2026-04-17/reasoning.md#execution-first-evaluation-is-replacing-answer-only-benchmarking)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [GeoAgentBench](https://arxiv.org/abs/2604.13888)
Implementable now:
- add parameter-level execution metrics to internal evals
- benchmark recovery loops explicitly
- verify outputs in the modality that matters
- normalize tool traces into a common event schema
Tools, repos, and methodologies worth exploring:
- [ClawBench](https://arxiv.org/abs/2604.08523v1)
- [Trace-tree debugging paper](https://arxiv.org/abs/2604.11641)
- [Tool-use representation paper](https://arxiv.org/abs/2604.11557)
- execution-sandbox eval harnesses
- plan-versus-react scorecards
Implementability score: 0.82

### Embeddable agent kernels are the right product shape for coding agents
Summary: Sema Code’s main contribution is architectural: the agent core should be reusable infrastructure that multiple client surfaces can drive, not intelligence trapped in one interface.

Analysis: [reasoning analysis](2026-04-17/reasoning.md#embeddable-agent-kernels-are-the-right-product-shape-for-coding-agents)
Durable topic: [Embeddable Agent Kernels](embeddable-agent-kernels/embeddable-agent-kernels.md)
Core source: [Sema Code](https://arxiv.org/abs/2604.11045)
Implementable now:
- separate the reasoning kernel from IDE, CLI, and messaging surfaces
- centralize permissions, task state, and long-running execution in the shared core
- expose typed APIs instead of burying behavior inside one product shell
- keep clients thin and replaceable
Tools, repos, and methodologies worth exploring:
- [sema-code-core](https://github.com/midea-ai/sema-code-core)
- [sema-code-vscode-extension](https://github.com/midea-ai/sema-code-vscode-extension)
- kernel-plus-client architecture
- MCP and skills as extension surfaces
Implementability score: 0.88

# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-19

### Workflow-level serving is becoming the new orchestration bottleneck
Summary: Scepsy is the clearest sign in this window that multi-LLM agents need workflow-level resource planning. The right optimization target is the aggregate execution path, not each model in isolation.

Analysis: [reasoning analysis](2026-04-19/reasoning.md#workflow-level-serving-is-becoming-the-new-orchestration-bottleneck)
Core source: [Scepsy](https://arxiv.org/abs/2604.15186)
Implementable now:
- profile which models dominate total workflow execution share across representative runs
- allocate GPUs against end-to-end bottlenecks instead of isolated model benchmarks
- plan tensor parallelism, replica counts, and placement together
- watch workflow latency and tail behavior directly before scaling replicas
Tools, repos, and methodologies worth exploring:
- [Scepsy paper](https://arxiv.org/abs/2604.15186)
- aggregate-LLM-pipeline planning
- workflow-level GPU allocation
- topology-aware placement heuristics
- end-to-end latency tracing for multi-LLM paths
Implementability score: 0.68

### Prompt optimization is a preflight decision, not a reflex
Summary: Prompt optimization in compound systems only pays when there is real structural headroom. Cheap diagnostics are a better default than blindly launching another DSPy or TextGrad search loop.

Analysis: [reasoning analysis](2026-04-19/reasoning.md#prompt-optimization-is-a-preflight-decision-not-a-reflex)
Core source: [Prompt Optimization Is a Coin Flip](https://arxiv.org/abs/2604.14585)
Implementable now:
- run a fast coupling test before assuming prompt interactions need joint optimization
- add a headroom check before spending compute on search
- optimize output schemas and intermediate artifacts before prompt wording
- keep zero-shot as a real control in the eval loop
Tools, repos, and methodologies worth exploring:
- [DSPy](https://github.com/stanfordnlp/dspy)
- [TextGrad](https://github.com/zou-group/textgrad)
- ANOVA-style agent coupling tests
- output-headroom diagnostics
- schema-first intermediate design
Implementability score: 0.92

### AG2 turns delegation, local execution, and observability into one operator surface
Summary: AG2 v0.12.0 is a strong open-source framework signal because it bundles the right primitives together: agent delegation via tool calls, subscribable observer events, local shell execution, and skill discovery.

Analysis: [reasoning analysis](2026-04-19/reasoning.md#ag2-turns-delegation-local-execution-and-observability-into-one-operator-surface)
Core source: [AG2 v0.12.0](https://github.com/ag2ai/ag2/releases/tag/v0.12.0)
Implementable now:
- wrap narrow subagents as tools instead of giving every agent broad chat authority
- instrument event streams before scaling multi-agent workflows
- use bounded local execution surfaces for operator-controlled tasks
- package reusable skills instead of cloning prompt blobs
Tools, repos, and methodologies worth exploring:
- [ag2ai/ag2](https://github.com/ag2ai/ag2)
- Agent.as_tool delegation patterns
- Observer API event tracing
- LocalShellTool and LocalShellEnvironment
- skills-as-reusable-procedure packaging
Implementability score: 0.89

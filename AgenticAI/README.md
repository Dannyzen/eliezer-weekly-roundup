# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-15

### Deep Dive Wednesday winner: File-as-Bus workspaces are becoming the practical substrate for long-horizon agents
Summary: The strongest implementation signal this week is that durable workspace artifacts are beating conversational handoff. AiScientist makes the case cleanly: if the run cannot survive through files, logs, plans, and validation artifacts, it is not really built for long-horizon work.

Analysis: [reasoning analysis](2026-04-15/reasoning.md#deep-dive-wednesday-winner)
Durable topic: [File-as-Bus Workspaces](file-as-bus-workspaces/file-as-bus-workspaces.md)
Core source: [Toward Autonomous Long-Horizon Engineering for ML Research](https://arxiv.org/abs/2604.13018)
Implementable now:
- use a workspace map as the entry point into long-running project state
- require delegated tasks to name read sets, write sets, and verification targets
- keep plans, experiment logs, and validation outputs as durable files
- permission-scope who can edit which artifacts
Tools, repos, and methodologies worth exploring:
- [AiScientist](https://github.com/AweAI-Team/AiScientist)
- [PaperBench](https://github.com/openai/frontier-evals/tree/main/project/paperbench)
- [MLE-Bench](https://github.com/openai/mle-bench)
- artifact-first delegation
- workspace maps
Implementability score: 0.92

### Dual-trace memory is a better design pattern than flat factual memory for cross-session agents
Summary: Memory quality improves when stored facts carry contextual scene traces. That is the difference between remembering a sentence and remembering when it became true.

Analysis: [reasoning analysis](2026-04-15/reasoning.md#dual-trace-memory-is-a-better-design-pattern-than-flat-factual-memory-for-cross-session-agents)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [Drawing on Memory: Dual-Trace Encoding Improves Cross-Session Recall in LLM Agents](https://arxiv.org/abs/2604.12948)
Implementable now:
- pair durable facts with source, timing, and local context traces
- evaluate memory on update tracking and multi-session aggregation instead of only one-hop recall
- add explicit write schemas for fact fields versus scene fields
- use temporal reasoning tests to validate persistent memory quality
Tools, repos, and methodologies worth exploring:
- [Drawing on Memory](https://arxiv.org/abs/2604.12948)
- [Memory Systems deep dive](memory-systems/memory-systems.md)
- LongMemEval-style benchmarks
- temporal memory QA suites
- dual-trace memory objects
Implementability score: 0.83

### Installable memory infrastructure is beating hidden prompt residue
Summary: The best open-source memory signal this week is not just a theory paper. It is `claude-mem`, which treats persistence as observable infrastructure with hooks, search, citations, and privacy controls.

Analysis: [reasoning analysis](2026-04-15/reasoning.md#installable-memory-infrastructure-is-beating-hidden-prompt-residue)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [claude-mem](https://github.com/thedotmack/claude-mem)
Implementable now:
- adopt search-first, fetch-details-second memory retrieval
- attach IDs and citations to retrieved memories
- split capture, consolidation, and retrieval into separate runtime stages
- make privacy exclusions explicit when memory is written
Tools, repos, and methodologies worth exploring:
- [claude-mem](https://github.com/thedotmack/claude-mem)
- progressive disclosure retrieval
- hybrid vector plus keyword memory search
- hook-based session instrumentation
- operator-facing memory viewers
Implementability score: 0.95

### Many-tier instruction hierarchy is the week’s sharpest agent-safety benchmark signal
Summary: Real agents receive instructions from many sources with different authority levels. ManyIH shows current models still degrade badly when that hierarchy gets realistic.

Analysis: [reasoning analysis](2026-04-15/reasoning.md#many-tier-instruction-hierarchy-is-the-weeks-sharpest-agent-safety-benchmark-signal)
Core source: [Many-Tier Instruction Hierarchy in LLM Agents](https://arxiv.org/abs/2604.09443)
Implementable now:
- annotate instruction sources with authority metadata
- model privilege outside the raw prompt text when side effects matter
- test multi-tier conflict resolution instead of only system-vs-user toy cases
- keep tool and delegated-agent outputs from silently inheriting user authority
Tools, repos, and methodologies worth exploring:
- [ManyIH paper](https://arxiv.org/abs/2604.09443)
- privilege-annotated prompt assembly
- multi-tier instruction conflict tests
- out-of-band policy enforcement
Implementability score: 0.61
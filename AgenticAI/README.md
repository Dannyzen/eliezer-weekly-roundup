# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-13

### Memory compression is turning into installable workflow infrastructure
Summary: The strongest implementation signal today was memory becoming a product surface instead of a hidden prompt trick. Installable tooling now captures observations, compresses them, exposes search, and adds privacy controls around what becomes durable.

Analysis: [reasoning analysis](2026-04-13/reasoning.md#memory-compression-is-turning-into-installable-workflow-infrastructure)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [claude-mem](https://github.com/thedotmack/claude-mem)
Implementable now:
- store observations and tool outcomes separately from polished summaries
- expose searchable memory with citations so operators can inspect evidence
- add exclusion or privacy controls before durable memory writes
- use layered retrieval instead of dumping giant transcript summaries back into context
Tools, repos, and methodologies worth exploring:
- [claude-mem](https://github.com/thedotmack/claude-mem)
- observation-first memory schemas
- progressive disclosure retrieval
- citation-backed memory review
- policy-gated memory writes
Implementability score: 0.95

### Managed agents are becoming workflow-native instead of prompt-native
Summary: The best orchestration signal today is not a new model. It is open-source tooling that treats agents like assignable teammates with runtimes, queues, blockers, and reusable skills.

Analysis: [reasoning analysis](2026-04-13/reasoning.md#managed-agents-are-becoming-workflow-native-instead-of-prompt-native)
Core source: [Multica](https://github.com/multica-ai/multica)
Implementable now:
- route agent work through tickets or issues instead of free-form chat
- require explicit lifecycle states such as queued, claimed, blocked, and complete
- turn repeated solutions into reusable skills
- separate planner, executor, and reviewer responsibilities in the workflow
Tools, repos, and methodologies worth exploring:
- [Multica](https://github.com/multica-ai/multica)
- issue-backed agent queues
- local-plus-cloud runtime routing
- reusable skill registries
- workflow boards with blocker reporting
Implementability score: 0.93

### Selective escalation is now a benchmarkable agent skill
Summary: Better agent evaluation is starting to measure whether the system knew it should ask for help, not just whether it got lucky on a fully specified task.

Analysis: [reasoning analysis](2026-04-13/reasoning.md#selective-escalation-is-now-a-benchmarkable-agent-skill)
Core source: [HiL-Bench paper](https://arxiv.org/abs/2604.09408)
Implementable now:
- add blocker detection and clarification steps to agent workflows
- score escalation quality separately from raw task completion
- build escalation templates for missing or contradictory requirements
- review silent-guess failures as their own failure class
Tools, repos, and methodologies worth exploring:
- [HiL-Bench](https://arxiv.org/abs/2604.09408)
- Ask-F1-style escalation metrics
- ambiguity-focused eval corpora
- approval checkpoints for under-specified work
- escalation postmortems
Implementability score: 0.78

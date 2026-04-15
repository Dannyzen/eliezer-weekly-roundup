# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-15

### File-as-Bus workspaces are becoming the practical substrate for long-horizon research agents
Summary: The strongest implementation signal today is that durable workspace artifacts are beating conversational handoff. Long-horizon agents work better when plans, code, experiments, and summaries are first-class shared state.

Analysis: [reasoning analysis](2026-04-15/reasoning.md#file-as-bus-workspaces-are-becoming-the-practical-substrate-for-long-horizon-research-agents)
Durable topic: [File-as-Bus Workspaces](file-as-bus-workspaces/file-as-bus-workspaces.md)
Core source: [Toward Autonomous Long-Horizon Engineering for ML Research](https://arxiv.org/abs/2604.13018)
Implementable now:
- move plans, experiment results, and decision logs into durable workspace artifacts
- keep the orchestrator thin and force specialists to re-ground on files instead of transcript residue
- use workspace maps and stage summaries to coordinate parallel work
- permission-scope artifact ownership to reduce multi-agent collisions
Tools, repos, and methodologies worth exploring:
- [AiScientist](https://github.com/AweAI-Team/AiScientist)
- file-as-bus workspaces
- artifact-first delegation
- stage-gated orchestration
- PaperBench and MLE-Bench Lite loops
Implementability score: 0.91

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
Summary: The best open-source memory signal today is not a theory paper. It is `claude-mem`, which treats persistence as observable infrastructure with hooks, search, citations, and privacy controls.

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

### Sequential routing is finally treating multi-turn dialogue as a control problem
Summary: Routing quality should be judged across a conversation, not one turn at a time. The stronger pattern is using sequential policies that trade off cumulative reward against cumulative cost.

Analysis: [reasoning analysis](2026-04-15/reasoning.md#sequential-routing-is-finally-treating-multi-turn-dialogue-as-a-control-problem-instead-of-a-single-turn-leaderboard-trick)
Core source: [From Myopic Selection to Long-Horizon Awareness: Sequential LLM Routing for Multi-Turn Dialogue](https://arxiv.org/abs/2604.12385)
Implementable now:
- evaluate routing on cumulative trajectory reward instead of isolated turns
- log dialogue-state features that predict downstream leverage
- reserve expensive models for turns that change later outcomes
- train routing policies offline from searched or replayed trajectories
Tools, repos, and methodologies worth exploring:
- [DialRouter paper](https://arxiv.org/abs/2604.12385)
- sequential routing policies
- MCTS-assisted route discovery
- cost-aware reward shaping
- offline routing from dialogue traces
Implementability score: 0.67
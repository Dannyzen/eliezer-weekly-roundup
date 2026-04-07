# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-07

### Springdrift treats auditable persistence as the actual runtime for long-lived agents
Summary: The important move is not more autonomy. It is a runtime substrate with append-only evidence, supervised processes, recovery paths, and deterministic safety gates.

Analysis: [sovereignty analysis](2026-04-07/sovereignty.md#springdrift-treats-auditable-persistence-as-the-actual-runtime-for-long-lived-agents)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [Springdrift: An Auditable Persistent Runtime for LLM Agents with Case-Based Memory, Normative Safety, and Ambient Self-Perception](https://arxiv.org/abs/2604.04660)
Implementable now:
- Add append-only runtime logs tied to agent identity and action lineage
- Keep recoverable state snapshots under versioned storage
- Put deterministic policy checks in front of memory writes and tool execution
- Record explicit self-state for diagnostics and replay
Implementability score: 0.62

### FileGram shows that local file activity is becoming a first-class memory substrate
Summary: File-system behavior may be a better source of personalization than chat summaries, but it only becomes strategically acceptable if the trace stays local and heavily scoped.

Analysis: [sovereignty analysis](2026-04-07/sovereignty.md#filegram-shows-that-local-file-activity-is-becoming-a-first-class-memory-substrate)
Core source: [FileGram: Grounding Agent Personalization in File-System Behavioral Traces](https://arxiv.org/abs/2604.04901)
Implementable now:
- Build privacy-scoped local event pipelines for file activity
- Infer working profiles from repeated behavioral traces, not only explicit preferences
- Separate procedural, semantic, and episodic memory channels
- Treat local behavioral traces as privileged infrastructure, not generic analytics exhaust
Implementability score: 0.58

# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-04-29

### Observability-driven harness evolution is the next coding-agent loop
Summary: AHE treats the coding-agent harness as an observable, editable, replayable artifact. The reusable pattern is to version harness components, distill long trajectories into usable evidence, pair each harness edit with a predicted effect, and verify that prediction against later task outcomes. GitHub Trending reinforced the demand signal with Warp, jcode, GitNexus, and skills repos all pointing toward agentic terminals, harnesses, skills, and code-graph context tools.

Analysis: [reasoning analysis](2026-04-29/reasoning.md#observability-driven-harness-evolution-is-the-next-coding-agent-loop)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [Agentic Harness Engineering](https://arxiv.org/abs/2604.25850v1)
Supporting sources:
- [jcode](https://github.com/1jehuang/jcode)
- [Warp](https://github.com/warpdotdev/warp)
- [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
- [Matt Pocock Skills](https://github.com/mattpocock/skills)
- [Awesome Codex Skills](https://github.com/ComposioHQ/awesome-codex-skills)
Implementable now:
- put harness instructions, tool schemas, retry policy, and workflow contracts in versioned files
- log harness component versions with each run
- distill long traces into layered evidence with drill-down paths
- require harness changes to declare predicted effects before evaluation
- replay task suites before rolling scaffold changes into daily use
Tools, repos, and methodologies worth exploring:
- OpenTelemetry or LangSmith-style trace capture
- Terminal-Bench, SWE-bench-verified, and internal replay suites
- git-backed harness component directories
- jcode, Warp, GitNexus, and skills repos as product-shape references
Implementability score: 0.72

### Knowledge-state orchestration is the missing layer for long-horizon synthesis
Summary: ADEMA argues that long-horizon agents fail because knowledge state drifts, intermediate commitments stay implicit, and interruptions break the evidence chain. The actionable pattern is to represent claims, evidence, assumptions, open questions, contradictions, artifacts, and checkpoints as explicit state rather than letting them live only in a transcript.

Analysis: [reasoning analysis](2026-04-29/reasoning.md#knowledge-state-orchestration-is-the-missing-layer-for-long-horizon-synthesis)
Durable topic: [Knowledge-State Orchestration](knowledge-state-orchestration/knowledge-state-orchestration.md)
Core source: [ADEMA](https://arxiv.org/abs/2604.25849v1)
Implementable now:
- store claim/evidence/assumption/question records as typed state
- checkpoint after each meaningful source-gathering, synthesis, or artifact phase
- keep source-backed notes separate from final prose
- run transition checks before accepting durable conclusions
- require final reports to link claims back to evidence artifacts
Tools, repos, and methodologies worth exploring:
- SQLite/Postgres typed state stores
- LangGraph or Temporal-style resumable workflows
- repo-backed research artifacts
- source-grounded claim/evidence tables
- final-validity checklists over stored state
Implementability score: 0.58

# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-11

### Runtime composition is becoming explicit engineering, not framework folklore
Summary: The strongest implementation signal today was frameworks turning wrapper order, lifecycle hooks, and compaction into explicit runtime controls instead of leaving them as incidental framework behavior.

Analysis: [reasoning analysis](2026-04-11/reasoning.md#runtime-composition-is-becoming-explicit-engineering-not-framework-folklore)
Core source: [pydantic/pydantic-ai v1.80.0 release](https://github.com/pydantic/pydantic-ai/releases/tag/v1.80.0)
Implementable now:
- make middleware and wrapper order explicit in runtime contracts
- regression-test safety, tracing, caching, and approval behavior under reordered execution
- expose lifecycle hooks for policy and telemetry attachment
- treat compaction as a configurable runtime feature with behavioral tests
Tools, repos, and methodologies worth exploring:
- [PydanticAI](https://github.com/pydantic/pydantic-ai)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- ordered middleware or capability graphs
- OpenTelemetry lifecycle spans
- compaction regression tests
Implementability score: 0.95

### Replayable agent operations are becoming operator-facing, not hidden internals
Summary: Checkpoints are maturing from buried implementation detail into an operator surface with branching, lineage, editable replays, and better token accounting.

Analysis: [reasoning analysis](2026-04-11/reasoning.md#replayable-agent-operations-are-becoming-operator-facing-not-hidden-internals)
Core source: [crewAI 1.14.2a2 release](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2a2)
Implementable now:
- store checkpoints in formats you can migrate, diff, and branch safely
- build lineage views for resumed and repaired runs
- let operators edit replay inputs instead of forcing cold restarts
- track reasoning-token and cache effects alongside standard token counts
Tools, repos, and methodologies worth exploring:
- [CrewAI](https://github.com/crewAIInc/crewAI)
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- checkpoint diff viewers
- replay and postmortem runbooks
Implementability score: 0.90

### Personal-agent evaluation is finally testing preference inference and intervention timing
Summary: Better benchmarks are exposing the gap between interface competence and trustworthy assistance by testing hidden preferences, proactive intervention, consent negotiation, and restraint.

Analysis: [reasoning analysis](2026-04-11/reasoning.md#personal-agent-evaluation-is-finally-testing-preference-inference-and-intervention-timing)
Core source: [KnowU-Bench paper](https://arxiv.org/abs/2604.08455v1)
Implementable now:
- add missing-preference and vague-instruction scenarios to evals
- test whether agents clarify before acting under ambiguity
- score proactive systems on post-rejection restraint
- separate GUI competence from trustworthy assistance in product metrics
Tools, repos, and methodologies worth exploring:
- Android emulator eval harnesses
- hidden-profile benchmarks
- trajectory judges for consent and restraint
- intervention-calibration metrics
Implementability score: 0.79

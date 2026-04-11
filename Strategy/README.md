# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-11

### Checkpoint persistence is now a security boundary
Summary: The most useful governance signal today was not a new safety paper. It was runtime frameworks treating checkpoint restore paths as part of the trust model.

Analysis: [sovereignty analysis](2026-04-11/sovereignty.md#checkpoint-persistence-is-now-a-security-boundary)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [microsoft/agent-framework python-1.0.1](https://github.com/microsoft/agent-framework/releases/tag/python-1.0.1)
Implementable now:
- audit checkpoint serialization and restore paths as security-critical code
- require explicit allowlists or typed schemas for restored state
- separate trusted framework state from extension state
- test restore paths with malicious or malformed fixtures
Tools, repos, and methodologies worth exploring:
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- restore-path security tests
- schema-first state formats
- append-only audit logs for checkpoint replay
Implementability score: 0.91

### Personalization without consent calibration is not trustworthy assistance
Summary: Personal-agent strategy still overrates task completion and underrates when the assistant asks, when it acts, and when it backs off.

Analysis: [sovereignty analysis](2026-04-11/sovereignty.md#personalization-without-consent-calibration-is-not-trustworthy-assistance)
Core source: [KnowU-Bench paper](https://arxiv.org/abs/2604.08455v1)
Implementable now:
- default to clarification under preference uncertainty
- add rejection-memory and cooldown logic for proactive systems
- score assistants on restraint and consent quality
- expose user controls for personalization scope and proactive behavior
Tools, repos, and methodologies worth exploring:
- hidden-profile eval suites
- intervention-threshold policy engines
- user-visible permission settings
- trace review for clarification and consent behavior
Implementability score: 0.76

# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-17

### Runtime governance is now a substrate choice, not a policy memo
Summary: The strategic shift this week is that governance lives in restore paths, sandbox boundaries, prompt-injection regressions, and instruction precedence — not in abstract policy documents.

Analysis: [sovereignty analysis](2026-04-17/sovereignty.md#runtime-governance-is-now-a-substrate-choice-not-a-policy-memo)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [microsoft/agent-framework python-1.0.1](https://github.com/microsoft/agent-framework/releases/tag/python-1.0.1)
Implementable now:
- audit checkpoint restore paths as security-sensitive interfaces
- run coding agents inside bounded sandboxes with explicit egress policy
- maintain prompt-injection and instruction-hierarchy regression suites
- model authority explicitly instead of flattening every instruction into one prompt
Tools, repos, and methodologies worth exploring:
- [Checkpoint security considerations](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints?pivots=programming-language-python#security-considerations)
- [PIArena](https://arxiv.org/abs/2604.08499v1)
- [mensfeld/code-on-incus](https://github.com/mensfeld/code-on-incus)
- [Many-tier instruction hierarchy benchmark](https://arxiv.org/abs/2604.09443)
- sandbox-first agent operations
Implementability score: 0.88

### Agent runtimes are consolidating into opinionated operating systems
Summary: Cloudflare’s Project Think is the clearest sign that the runtime itself is becoming the product. Persistence, subagents, sessions, and sandboxes are being bundled into an operating environment.

Analysis: [sovereignty analysis](2026-04-17/sovereignty.md#agent-runtimes-are-consolidating-into-opinionated-operating-systems)
Durable topic: [Governed Workflow Substrates](governed-workflow-substrates/governed-workflow-substrates.md)
Core source: [Project Think](https://blog.cloudflare.com/project-think/)
Implementable now:
- compare platforms on persistence, isolation, and idle-cost behavior
- design agents as durable identities rather than only request-response sessions
- isolate child agents with explicit state and privilege boundaries
- package retries and sandboxing as runtime features
Tools, repos, and methodologies worth exploring:
- [Cloudflare Agents docs](https://developers.cloudflare.com/agents/index.md)
- durable execution with resumable checkpoints
- wake-on-event runtimes
- isolated subagent storage
Implementability score: 0.72

### Personal-agent trust is still weak where consent and clarification matter
Summary: The hard part of personal agents is still human calibration. Current systems remain weak at preference inference, consent boundaries, and knowing when to ask before acting.

Analysis: [sovereignty analysis](2026-04-17/sovereignty.md#personal-agent-trust-is-still-weak-where-consent-and-clarification-matter)
Core source: [KnowU-Bench](https://arxiv.org/abs/2604.08455v1)
Implementable now:
- add clarification and post-rejection restraint tests to personal-agent evals
- separate inferred preferences from confirmed preferences
- reward selective escalation instead of penalizing all questions
- require uncertainty surfacing before high-consequence actions
Tools, repos, and methodologies worth exploring:
- [Selective escalation benchmark](https://arxiv.org/abs/2604.09408)
- consent-aware preference schemas
- clarification-first workflow design
- escalation-quality scorecards
Implementability score: 0.63

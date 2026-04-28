# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-04-28

### Symphony turns issue trackers into agent control planes
Summary: OpenAI's Symphony release is the clearest current example of ticket-native coding-agent orchestration. The useful pattern is not the Elixir implementation; it is the spec: poll an issue tracker, create an isolated workspace per issue, run a coding-agent session continuously, keep workflow policy in-repo, and expose enough logs/status for a human to manage work instead of sessions.

Analysis: [reasoning analysis](2026-04-28/reasoning.md#symphony-turns-issue-trackers-into-agent-control-planes)
Durable topic: [Ticket-Native Agent Orchestration](ticket-native-agent-orchestration/ticket-native-agent-orchestration.md)
Core source: [OpenAI Symphony announcement](https://openai.com/index/open-source-codex-orchestration-symphony)
Supporting sources:
- [openai/symphony](https://github.com/openai/symphony)
- [Symphony SPEC.md](https://github.com/openai/symphony/blob/main/SPEC.md)
- [Codex App Server](https://developers.openai.com/codex/app-server/)
Implementable now:
- use Linear, GitHub Issues, or another tracker as the durable task queue
- create per-ticket workspaces with explicit cleanup and stop semantics
- put workflow rules in `WORKFLOW.md` or an equivalent repo-owned contract
- attach CI status, PR links, review packets, and proof-of-work artifacts to the ticket
- start with trusted environments and add sandbox/approval posture explicitly
Tools, repos, and methodologies worth exploring:
- OpenAI Symphony spec and reference implementation
- Codex App Server or another programmatic agent runner
- Linear/GitHub Issues as state machines
- structured logs, OpenTelemetry spans, and workspace lifecycle hooks
Implementability score: 0.88

### Agent evaluation is moving to DAGs, deployment signals, and OS-agent stress tests
Summary: Three fresh papers point in the same direction: agent eval is becoming operational observability. AgentEval models workflows as DAGs for root-cause attribution, AgentPulse scores deployed agents across benchmark/adoption/sentiment/ecosystem signals, and OS-SPEAR evaluates OS agents across safety, performance, efficiency, and robustness.

Analysis: [reasoning analysis](2026-04-28/reasoning.md#agent-evaluation-is-moving-to-dags-deployment-signals-and-os-agent-stress-tests)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [AgentEval](https://arxiv.org/abs/2604.23581)
Supporting sources:
- [AgentPulse](https://arxiv.org/abs/2604.24038)
- [OS-SPEAR](https://arxiv.org/abs/2604.24348)
- [Wuzheng02/OS-SPEAR](https://github.com/Wuzheng02/OS-SPEAR)
Implementable now:
- represent workflow traces as DAGs with typed node metrics and dependency edges
- score intermediate failures, not only final outputs
- collect deployment health signals such as issue velocity, package usage, sentiment, and ecosystem activity
- separate OS-agent safety, latency/token cost, performance, and robustness perturbation tests
Tools, repos, and methodologies worth exploring:
- AgentEval-style hierarchical failure taxonomies
- AgentPulse-style multi-signal dashboards
- OS-SPEAR safety/performance/efficiency/robustness subsets
- CI/CD regression gates over replayable traces
Implementability score: 0.76

### Skill repositories need retrieval gates and machine-readable structure
Summary: Skill Retrieval Augmentation and SSL skill representation both attack the same failure mode: dumping every skill into context does not scale. Agents need a skill registry that retrieves candidates, decides whether loading is actually necessary, and exposes scheduling, structural, logical, and risk evidence in a machine-readable form.

Analysis: [reasoning analysis](2026-04-28/reasoning.md#skill-repositories-need-retrieval-gates-and-machine-readable-structure)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [Skill Retrieval Augmentation for Agentic AI](https://arxiv.org/abs/2604.24594)
Supporting sources:
- [From Skill Text to Skill Structure](https://arxiv.org/abs/2604.24026)
Implementable now:
- store skill metadata separately from full skill bodies
- retrieve a small candidate set, then gate loading on task fit and external-capability need
- normalize skill artifacts into invocation interfaces, execution structure, side effects, and risk tags
- log which retrieved skills were loaded and whether they improved task outcomes
Tools, repos, and methodologies worth exploring:
- embedding plus lexical retrieval over skills
- rerankers and applicability classifiers
- structured skill schemas inspired by SSL
- regression tests that compare text-only skill lookup against structured lookup
Implementability score: 0.70

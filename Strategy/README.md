# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-09

### TraceSafe shows that agent safety has to be tested inside the trajectory, not just at the output boundary
Summary: The important result is not that another guardrail benchmark exists. It is that mid-trajectory risk detection depends heavily on structured-trace competence, which means most current safety rhetoric is aimed at the wrong surface.

Analysis: [sovereignty analysis](2026-04-09/sovereignty.md#tracesafe-shows-that-agent-safety-has-to-be-tested-inside-the-trajectory-not-just-at-the-output-boundary)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories](https://arxiv.org/abs/2604.07223)
Implementable now:
- benchmark guardrails against full tool-call traces, not just final model responses
- validate structured parsing and trace understanding before assuming a safety model can govern agents
- instrument policy checks at each tool step instead of only pre-prompt and post-response
- store evidence artifacts that explain why a guardrail flagged or allowed a step
Tools, repos, and methodologies worth exploring:
- [TraceSafe paper](https://arxiv.org/abs/2604.07223)
- trace-linked policy engines and approval middleware
- JSON- and schema-focused robustness tests for guardrails
Implementability score: 0.74

### AgentCity is a useful strategic provocation about multi-principal accountability, not a deployment recipe
Summary: The paper matters less as a blockchain pitch than as a forcing function. Once agents transact across principals, somebody has to own the chain from policy to action to adjudication.

Analysis: [sovereignty analysis](2026-04-09/sovereignty.md#agentcity-is-a-useful-strategic-provocation-about-multi-principal-accountability-not-a-deployment-recipe)
Core source: [AgentCity: Constitutional Governance for Autonomous Agent Economies via Separation of Power](https://arxiv.org/abs/2604.07007)
Implementable now:
- model agent accountability chains explicitly even if you never touch a blockchain
- separate policy authorship, action execution, and human adjudication into different operational roles
- require every autonomous agent to resolve to a responsible principal
- test governance for cross-organization delegation before scale forces the issue
Tools, repos, and methodologies worth exploring:
- explicit principal binding for agent identities
- approval and arbitration workflows for inter-agent transactions
- policy-as-code plus event-sourced audit logs
Implementability score: 0.24

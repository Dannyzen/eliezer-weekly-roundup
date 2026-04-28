# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-04-28

### Agent security is becoming lifecycle governance plus semantic privilege separation
Summary: AgentWard, AgentVisor, RiskGate, and OpenAI Privacy Filter all point to the same strategic move: security for agents has to sit in the runtime path. The stack needs lifecycle controls across startup, input, memory, decision, and execution; a trusted mediator for tool calls; adaptive monitoring for drift; and local PII filtering before sensitive context reaches a model or tool.

Analysis: [sovereignty analysis](2026-04-28/sovereignty.md#agent-security-is-becoming-lifecycle-governance-plus-semantic-privilege-separation)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [AgentWard](https://arxiv.org/abs/2604.24657)
Supporting sources:
- [FIND-Lab/AgentWard](https://github.com/FIND-Lab/AgentWard)
- [AgentVisor](https://arxiv.org/abs/2604.24118)
- [Governing What You Cannot Observe](https://arxiv.org/abs/2604.24686)
- [OpenAI Privacy Filter](https://openai.com/index/introducing-openai-privacy-filter/)
- [openai/privacy-filter](https://github.com/openai/privacy-filter)
Implementable now:
- add a policy mediator in front of privileged tool calls
- separate foundation scan, input sanitization, memory protection, decision alignment, and execution control
- run local PII filtering/redaction before agent context is stored, retrieved, or sent upstream
- track drift and anomaly signals as runtime governance evidence, not only postmortem analytics
Tools, repos, and methodologies worth exploring:
- AgentWard's OpenClaw plugin architecture
- AgentVisor-style semantic privilege separation
- RiskGate-style monotonic restriction and viability indices
- OpenAI Privacy Filter for local redaction and context minimization
- OPA/Cedar policies and trace-linked evidence capture
Implementability score: 0.64

# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-12

### Prompt injection defense is becoming an evaluation platform problem, not a single-paper claim
Summary: The most useful governance signal today was a platform view of prompt injection: defenses need to survive adaptive attacks, cross-task transfer, and realistic deployment conditions, not just isolated benchmarks.

Analysis: [sovereignty analysis](2026-04-12/sovereignty.md#prompt-injection-defense-is-becoming-an-evaluation-platform-problem-not-a-single-paper-claim)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [PIArena paper](https://arxiv.org/abs/2604.08499v1)
Implementable now:
- build standing prompt-injection regression suites
- test defenses against adaptive attacks instead of static strings
- evaluate across multiple tasks, tools, and retrieval settings
- track graceful degradation versus catastrophic failure
Tools, repos, and methodologies worth exploring:
- [PIArena](https://arxiv.org/abs/2604.08499v1)
- [TraceSafe](https://arxiv.org/abs/2604.07223)
- attack corpora with task-alignment variation
- policy mediation ahead of tool execution
Implementability score: 0.84

### Hardened execution isolation is becoming the sane default for coding agents
Summary: The strongest sovereignty signal today was practical sandboxing: run coding agents inside bounded, inspectable, interruptible environments instead of your main workstation identity.

Analysis: [sovereignty analysis](2026-04-12/sovereignty.md#hardened-execution-isolation-is-becoming-the-sane-default-for-coding-agents)
Durable topic: [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md)
Core source: [code-on-incus](https://github.com/mensfeld/code-on-incus)
Implementable now:
- use dedicated non-admin users or hardened containers for coding agents
- keep SSH keys, cloud credentials, and host-wide env vars out of the runtime
- add egress controls for agents that do not need arbitrary outbound access
- preserve pause, kill, and workspace-inspection controls for incident response
Tools, repos, and methodologies worth exploring:
- [code-on-incus](https://github.com/mensfeld/code-on-incus)
- [Running AI agents in a sandbox](https://oligot.be/posts/ai-sandbox/)
- Incus or LXC-based workspaces
- proxy-mediated egress controls
- protected path policies
Implementability score: 0.89

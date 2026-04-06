# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-05

### Runtime governance is solidifying into a real product category
Summary: Microsoft's Agent Governance Toolkit is important because it frames governance as execution-layer infrastructure with policy interception, identity, execution rings, SRE controls, and compliance evidence instead of after-the-fact policy docs.

Analysis: [sovereignty analysis](2026-04-05/sovereignty.md#runtime-governance-is-solidifying-into-a-real-product-category)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [Microsoft Open Source Blog, April 2, 2026](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/)
Implementable now:
- Put a policy layer between agents and tools
- Treat agents as services with identity, scopes, and kill switches
- Map live workflows against OWASP agentic AI risks
- Build governance evidence collection into runtime traces
Implementability score: 0.86

### Persistent memory has become a first-class attack surface
Summary: The eTAMP paper on environment-injected memory poisoning makes the practical point that memory is not a helpful add-on. It is a cross-session trust boundary that can be poisoned without direct access to the memory store.

Analysis: [sovereignty analysis](2026-04-05/sovereignty.md#persistent-memory-has-become-a-first-class-attack-surface)
Core source: [Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents](https://arxiv.org/abs/2604.02623)
Implementable now:
- Treat memory writes like tool actions with policy and review controls
- Add provenance, TTLs, and trust scores to stored memories
- Separate raw observation storage from reusable long-term memory
- Run red-team scenarios for cross-session memory contamination
Implementability score: 0.72

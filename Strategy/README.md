# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-19

### Hybrid routing is becoming a sovereignty lever, not just a cost optimization
Summary: Atropos plus current product and tooling releases point to the same lesson: local-first works best when you own the escalation policy. Smaller or local models should do the easy and sensitive work first, then stronger models should take over only when the evidence says they need to.

Analysis: [sovereignty analysis](2026-04-19/sovereignty.md#hybrid-routing-is-becoming-an-architecture-choice-not-a-cost-hack)
Durable topic: [Local-First Agents](local-first-agents/local-first-agents.md)
Core source: [Atropos](https://arxiv.org/abs/2604.15075)
Implementable now:
- route bounded or sensitive tasks to smaller or local models first
- escalate only when midpoint evidence predicts failure or policy requires more capability
- log why a task escalated and which model completed it
- keep routing policy auditable instead of burying it in provider defaults
Tools, repos, and methodologies worth exploring:
- [Atropos](https://arxiv.org/abs/2604.15075)
- [GitHub Copilot CLI auto model selection](https://github.blog/changelog/2026-04-17-github-copilot-cli-now-supports-copilot-auto-model-selection/)
- [Vessel Browser](https://huggingface.co/blog/unmodeled-tyler/vessel-browser-for-agents)
- failure-prediction-based hotswap routing
- escalation logging and policy dashboards
Implementability score: 0.79

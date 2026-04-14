# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-14

### Agent cloud substrates are becoming a platform layer
Summary: The strongest strategy signal today is that runtime substrate is becoming a product category. Cloudflare's latest Agent Cloud push treats long-running agents as an infrastructure problem involving cheap isolation, durable storage, and deployable sandboxes.

Analysis: [sovereignty analysis](2026-04-14/sovereignty.md#agent-cloud-substrates-are-becoming-a-platform-layer)
Durable topic: [Governed Workflow Substrates](governed-workflow-substrates/governed-workflow-substrates.md)
Core source: [Cloudflare Agent Cloud press release](https://www.cloudflare.com/press/press-releases/2026/cloudflare-expands-its-agent-cloud-to-power-the-next-generation-of-agents/)
Implementable now:
- separate cheap ephemeral execution from heavier long-lived environments
- give agents durable storage that stays legible to Git and developer workflows
- run agents inside killable, inspectable sandboxes instead of privileged always-on pets
- plan for many short agent actions rather than a few giant sessions
Tools, repos, and methodologies worth exploring:
- [Cloudflare Agent Cloud](https://www.cloudflare.com/press/press-releases/2026/cloudflare-expands-its-agent-cloud-to-power-the-next-generation-of-agents/)
- Dynamic Workers
- Git-compatible artifact stores
- agent-specific sandboxes
- isolate-first execution design
Implementability score: 0.74

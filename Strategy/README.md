# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-04-25

### Agent boundary safety is moving into SDK defaults and adversarial test loops
Summary: The strongest strategic signal today is that safety for high-autonomy agents must live below the prompt: sensitive-path blocking, portable permission profiles, session-level moderation, sandboxed browsing, and evidence bundles.

Analysis: [sovereignty analysis](2026-04-25/sovereignty.md#agent-boundary-safety-is-moving-into-sdk-defaults-and-adversarial-test-loops)
Core source: [Composio Python 0.11.6](https://github.com/ComposioHQ/composio/releases/tag/py%400.11.6)
Supporting sources:
- [OpenAI Codex 0.125.0](https://github.com/openai/codex/releases/tag/rust-v0.125.0)
- [Transient Turn Injection](https://arxiv.org/abs/2604.21860v1)
- [TraceScope](https://arxiv.org/abs/2604.21840v1)
- [OpenAI Agents Python v0.14.5](https://github.com/openai/openai-agents-python/releases/tag/v0.14.5)
Implementable now:
- block `.ssh`, `.aws`, token files, and other sensitive paths before any agent-managed file upload
- require file-upload hooks in tool routers that touch local files
- attach serializable permission profiles to every tool call and resumed session
- test stateless moderation against multi-turn attack fixtures
- run high-risk browser/tool agents in disposable sandboxes with evidence bundles
Tools, repos, and methodologies worth exploring:
- Composio sensitive file upload protection
- Codex permission profiles and app-server session APIs
- multi-turn adversarial testing inspired by Transient Turn Injection
- sandboxed operator-agent pipelines inspired by TraceScope
- secret/path canaries in CI for agent tool integrations
Implementability score: 0.78

# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-06

### Gemma 4 plus LiteRT-LM makes local-first multimodal agents a real design option
Summary: Gemma 4 and LiteRT-LM together make local-first agent design materially more practical: open multimodal models, tool calling, constrained decoding, CLI support, and deployment paths across phones, desktops, browsers, and edge devices.

Analysis: [sovereignty analysis](2026-04-06/sovereignty.md#gemma-4-plus-litert-lm-makes-local-first-multimodal-agents-a-real-design-option)
Durable topic: [Local-First Agents](local-first-agents/local-first-agents.md)
Core source: [Bring state-of-the-art agentic skills to the edge with Gemma 4](https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/)
Implementable now:
- Prototype private or latency-sensitive subtasks on Gemma 4 before defaulting to hosted APIs
- Use LiteRT-LM for local inference, structured outputs, and tool calling
- Use Google AI Edge Gallery to test on-device agent skills quickly
- Add a routing policy that only escalates to cloud models when needed
Implementability score: 0.91

### OpenClaw security evaluation is a warning about the entire agent lifecycle
Summary: A 205-case security benchmark across six OpenClaw-series frameworks shows that once an agent gains tools and persistent runtime context, the system risk exceeds the model risk in isolation.

Analysis: [sovereignty analysis](2026-04-06/sovereignty.md#openclaw-security-evaluation-is-a-warning-about-the-entire-agent-lifecycle-not-one-framework)
Core source: [A Systematic Security Evaluation of OpenClaw and Its Variants](https://arxiv.org/abs/2604.03131)
Implementable now:
- Expand red-team testing from prompts to full multi-step agent execution
- Put policy and approval gates in front of tools and long-lived context
- Separate trust tiers for credentials, ephemeral context, and durable memory
- Treat framework choice as a security architecture decision
Implementability score: 0.66

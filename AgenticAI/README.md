# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-12

### Workflow-defined AI coding is becoming a real product category
Summary: The strongest implementation signal today was not a new model trick. It was open-source tooling pushing teams to encode planning, validation, and delivery as explicit agent workflows instead of trusting one-shot prompting.

Analysis: [reasoning analysis](2026-04-12/reasoning.md#workflow-defined-ai-coding-is-becoming-a-real-product-category)
Core source: [Archon](https://github.com/coleam00/Archon)
Implementable now:
- encode planning, implementation, testing, and review as explicit workflow phases
- require plans, test outputs, and diff summaries as gating artifacts
- version reusable agent instructions as skills or workflow steps
- standardize one narrow coding lane before expanding to more autonomy
Tools, repos, and methodologies worth exploring:
- [Archon](https://github.com/coleam00/Archon)
- [Multica](https://github.com/multica-ai/multica)
- YAML-defined agent workflows
- gated coding pipelines
- reusable skill libraries
Implementability score: 0.94

### Live-web evaluation is finally measuring what general-purpose assistants actually face
Summary: Better agent evaluation is shifting from toy sandboxes to live websites with side-effect blocking and multi-layer telemetry, which is much closer to what real assistants will actually fail on.

Analysis: [reasoning analysis](2026-04-12/reasoning.md#live-web-evaluation-is-finally-measuring-what-general-purpose-assistants-actually-face)
Core source: [ClawBench paper](https://arxiv.org/abs/2604.08523v1)
Implementable now:
- add final-action interception to evals that touch real services
- capture browser actions, screenshots, network traces, and model trajectories together
- score step quality separately from final completion
- build eval suites from routine but messy real user workflows
Tools, repos, and methodologies worth exploring:
- [ClawBench](https://claw-bench.com)
- [Hugging Face paper page](https://huggingface.co/papers/2604.08523)
- Playwright-based eval harnesses
- trace-linked screenshot and HTTP logging
- failure taxonomies for browsing agents
Implementability score: 0.86

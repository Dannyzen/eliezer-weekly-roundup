# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-09

### PydanticAI v1.78.0 makes tool contracts more explicit and more observable
Summary: The useful shift is not cosmetic. Tool definitions are getting richer enough to become durable runtime contracts instead of loose prompt conventions, while OpenTelemetry coverage keeps the orchestration layer inspectable.

Analysis: [reasoning analysis](2026-04-09/reasoning.md#pydanticai-v1780-makes-tool-contracts-more-explicit-and-more-observable)
Core source: [pydantic/pydantic-ai v1.78.0 release](https://github.com/pydantic/pydantic-ai/releases/tag/v1.78.0)
Implementable now:
- expose `return_schema` and `function_signature` in tool metadata instead of relying on prose descriptions alone
- attach per-tool metadata so downstream policy, logging, and UI layers can reason about tools as typed objects
- emit cached-token span attributes so agent cost and cache behavior show up in existing observability stacks
- treat tool definitions as versioned contracts that can be diffed and tested
Tools, repos, and methodologies worth exploring:
- [PydanticAI](https://github.com/pydantic/pydantic-ai)
- OpenTelemetry tracing for agent runs
- schema-diff checks for tool registries
Implementability score: 0.95

### ALTK-Evolve shows the right memory pattern: learn guidelines, not transcript sludge
Summary: The strongest memory lesson today is that replaying old transcripts into the prompt is a dead end. Better agents distill reusable operating guidance from traces and retrieve only what matters at action time.

Analysis: [reasoning analysis](2026-04-09/reasoning.md#altk-evolve-shows-the-right-memory-pattern-learn-guidelines-not-transcript-sludge)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [ALTK-Evolve: On-the-Job Learning for AI Agents](https://huggingface.co/blog/ibm-research/altk-evolve)
Implementable now:
- capture trajectories in an observability layer instead of throwing them away after a run
- extract candidate guidelines from traces and score them before promoting them to durable memory
- retrieve a small set of relevant rules at action time instead of pasting whole transcripts into context
- keep memory quality loops separate from the online action loop
Tools, repos, and methodologies worth exploring:
- [ALTK-Evolve article](https://huggingface.co/blog/ibm-research/altk-evolve)
- Langfuse or another OpenTelemetry-based trace layer
- offline consolidation jobs for memory pruning and scoring
Implementability score: 0.82

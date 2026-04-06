# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-05

### PydanticAI turns structured prompting into cheaper runtime behavior
Summary: PydanticAI's new smart instruction caching and thread execution support show a practical path to lower-cost agent loops without rebuilding the whole stack.

Analysis: [reasoning analysis](2026-04-05/reasoning.md#pydanticai-smart-instruction-caching-and-thread-execution)
Core source: [PydanticAI v1.77.0 release](https://github.com/pydantic/pydantic-ai/releases/tag/v1.77.0)
Implementable now:
- Split prompts into stable policy and dynamic task state
- Use cache-aware model calls for repeated agent loops
- Use thread executors for parallel tool-heavy steps
- Keep schemas typed with Pydantic models end to end
Implementability score: 0.93

### Langfuse is making agent evals tool-aware instead of answer-only
Summary: Langfuse added judge filters for tool names and tool-call count. That is a real shift from generic LLM scoring toward agent-specific evaluation.

Analysis: [reasoning analysis](2026-04-05/reasoning.md#langfuse-tool-aware-agent-evals)
Core source: [Langfuse v3.163.0 release](https://github.com/langfuse/langfuse/releases/tag/v3.163.0)
Implementable now:
- Add pass-fail checks for tool ordering and tool count
- Compare variants on answer quality and trajectory quality
- Use judge outputs as CI gates for critical workflows
- Track tool misuse as a first-class regression category
Implementability score: 0.94

### TensorZero is collapsing gateway, routing, and observability into one surface
Summary: TensorZero's new MCP gateway endpoint plus prompt cache and eval usage metrics point toward a tighter control plane for model routing and agent operations.

Analysis: [reasoning analysis](2026-04-05/reasoning.md#tensorzero-mcp-gateway-and-ops-metrics)
Core source: [TensorZero 2026.4.0 release](https://github.com/tensorzero/tensorzero/releases/tag/2026.4.0)
Implementable now:
- Put TensorZero in front of one agent workflow
- Export token, latency, and cache stats into Prometheus and Grafana
- Compare cheap-router versus expensive-fallback policies with eval telemetry
- Use MCP exposure to standardize tool access patterns
Implementability score: 0.89

### CrewAI is getting more serious about replayable runtime state
Summary: Unified runtime state serialization and telemetry spans for memory and skill events are exactly the kind of primitives needed for debugging and auditability.

Analysis: [reasoning analysis](2026-04-05/reasoning.md#crewai-runtime-state-and-memory-telemetry)
Core source: [CrewAI 1.13.0 release](https://github.com/crewAIInc/crewAI/releases/tag/1.13.0)
Implementable now:
- Persist runtime state per step for replay and debugging
- Instrument memory and skill events even outside CrewAI
- Attribute token usage at event boundaries
- Define owner-of-record for each subagent step
Implementability score: 0.88

### LangGraph is reinforcing the move from graphs that run to graphs you can inspect
Summary: Enhanced runtime execution information and remote deploy support show where serious orchestration is heading: inspectable state, standard deploy paths, and better debugging hooks.

Analysis: [reasoning analysis](2026-04-05/reasoning.md#langgraph-runtime-introspection-and-remote-builds)
Core source: [LangGraph v1.1.5 release](https://github.com/langchain-ai/langgraph/releases/tag/1.1.5)
Implementable now:
- Persist execution metadata alongside outputs
- Assert on state transitions in integration tests
- Standardize remote build environments for agent runs
- Treat runtime traces as part of the product, not just debugging exhaust
Implementability score: 0.86

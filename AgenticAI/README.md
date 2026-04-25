# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-04-25

### Agent runtimes are becoming evented app servers, not CLI loops
Summary: The latest framework and tool releases point to the same runtime shape: resumable sessions, sticky environments, process event streams, deferred tool calls, permission profiles, plugin APIs, and rollout traces. Agents are becoming app servers with state, not scripts around prompts.

Analysis: [reasoning analysis](2026-04-25/reasoning.md#agent-runtimes-are-becoming-evented-app-servers-not-cli-loops)
Core source: [OpenAI Codex 0.125.0](https://github.com/openai/codex/releases/tag/rust-v0.125.0)
Supporting sources:
- [Pydantic AI v1.87.0](https://github.com/pydantic/pydantic-ai/releases/tag/v1.87.0)
- [LangGraph prebuilt 1.0.11](https://github.com/langchain-ai/langgraph/releases/tag/prebuilt%3D%3D1.0.11)
- [AG2 v0.12.1](https://github.com/ag2ai/ag2/releases/tag/v0.12.1)
Implementable now:
- model each agent run as an evented state machine with resumable thread state
- preserve tool, permission, environment, human-approval, and model events as typed trace records
- expose reasoning-token usage and rollout traces to programmatic consumers
- use permission profiles as data structures that travel across sessions and shell escalation
Tools, repos, and methodologies worth exploring:
- OpenAI Codex app-server APIs and rollout traces
- Pydantic AI `ProcessEventStream` and `HandleDeferredToolCalls`
- LangGraph `ToolRuntime`
- AG2 step events and toolkit merging
- OpenTelemetry-style traces for tool and session lifecycle
Implementability score: 0.93

### Skills and grounding documents are becoming the deterministic control layer
Summary: New research on scientific workflows, GROUNDING.md, and reasoning skills converges on a practical pattern: let the LLM map intent, but use reviewed markdown skills, hard constraints, and deterministic generators to control execution.

Analysis: [reasoning analysis](2026-04-25/reasoning.md#skills-and-grounding-documents-are-becoming-the-deterministic-control-layer)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [From Research Question to Scientific Workflow](https://arxiv.org/abs/2604.21910v1)
Supporting sources:
- [GROUNDING.md for agentic coding](https://arxiv.org/abs/2604.21744v1)
- [Thinking with Reasoning Skills](https://arxiv.org/abs/2604.21764v1)
- [AEL: Agent Evolving Learning](https://arxiv.org/abs/2604.21725v1)
Implementable now:
- create repo, domain, and method-level `GROUNDING.md` or `SKILLS.md` files
- separate hard constraints from conventions, examples, and tests
- compile LLM intents into deterministic DAGs, scripts, or configs before execution
- promote repeated successes into reviewed skills instead of raw memory dumps
Tools, repos, and methodologies worth exploring:
- markdown skill libraries
- typed intent schemas
- deterministic workflow generators
- reasoning-skill retrieval
- skill regression tests
Implementability score: 0.86

### Learned latent multi-agent communication is a research signal, not an implementation default
Summary: DiffMAS shows that inter-agent communication may eventually be learned as a latent channel rather than written as verbose text handoffs. The practical takeaway today is narrower: make handoffs typed, measured, and traceable before adding more agents.

Analysis: [reasoning analysis](2026-04-25/reasoning.md#learned-latent-multi-agent-communication-is-a-research-signal-not-an-implementation-default)
Core source: [Learning to Communicate](https://arxiv.org/abs/2604.21794v1)
Implementable now:
- replace free-form inter-agent summaries with typed handoff schemas
- measure token cost, failure rate, and missing evidence at each handoff boundary
- preserve structured multi-agent traces for offline analysis
- test whether fewer agents with better state transfer beat more role prompts
Tools, repos, and methodologies worth exploring:
- typed handoff contracts in LangGraph, AG2, or custom orchestrators
- trajectory analysis by handoff boundary
- multi-agent ablation suites
- DiffMAS-style research tracking
Implementability score: 0.28

# Strategy analysis: 2026-04-10

Today's strategic signal is that sovereignty is not just about where the model runs. It is about whether the system can resist hostile instruction channels and whether its internal state belongs to the user or to a pile of disconnected apps. The strongest findings today sharpen those two questions.

## PIArena turns prompt injection defense into a real comparative evaluation problem
Source date: 2026-04-09  
Core source: https://arxiv.org/abs/2604.08499v1  
Durable deep dive: [Runtime Governance](../runtime-governance/runtime-governance.md)

PIArena matters because it attacks a problem the field keeps hand-waving. Prompt injection defense claims are usually benchmark-fragile, attack-fragile, or both. This paper introduces a unified and extensible evaluation platform that can integrate attacks and defenses across multiple benchmarks, and it adds a dynamic strategy-based attack that adapts based on defense feedback. The headline is ugly but useful: many defenses that look good in narrow settings generalize poorly across tasks and break under adaptive attacks.

Why it matters:
- Security claims without cross-benchmark evaluation are marketing, not governance.
- Adaptive attackers are the realistic case once agents touch tools, memory, browsing, or external content.
- Injection resilience is now a platform property. It depends on routing, tool mediation, parsing discipline, and context isolation as much as on the model itself.

How it fits into strategy:
- Governance layer: defenses need to be evaluated as runtime systems, not as isolated prompts.
- Security layer: adaptive attacks make static prompt hardening look weaker than many teams assume.
- Procurement layer: platform buyers should ask how a stack behaves under varied tasks and adaptive attack feedback, not just on one curated benchmark.

What is implementable now:
- run prompt injection tests across multiple task families instead of one internal demo set
- include adaptive attacks that mutate based on model or defense behavior
- measure defense generalization separately from headline attack-block rates
- combine prompt-layer defenses with tool scoping, retrieval isolation, and policy mediation

What remains conceptual:
- there is still no standard evaluation suite shared across major agent frameworks
- many defenses remain too task-specific to transfer cleanly

Practical tools, repos, and methodologies worth exploring:
- benchmark harnesses that pair attacks, defenses, and task families in one matrix
- tool-scoped execution sandboxes
- retrieval isolation for untrusted content channels
- runtime policy engines that can reject or rewrite risky actions even after an injection lands

Opinionated take:
Prompt injection is not a solved model problem. It is an unsolved systems problem, and PIArena is useful because it makes that failure measurable.

Implementability score: 0.76

## PSI argues that shared state is the missing sovereignty layer for personal agents
Source date: 2026-04-09  
Core source: https://arxiv.org/abs/2604.08529v1  
Durable deep dive: [Shared-State Agents](../shared-state-agents/shared-state-agents.md)

PSI is the most interesting sovereignty paper today because it reframes the problem correctly. Personal AI tools generated from natural language are not very useful if they stay isolated. PSI proposes a shared-state architecture where generated modules publish current state and write-back affordances to a personal-context bus, letting GUI tools and a generic chat agent operate on the same persistent artifacts. That is a much better frame than treating chat as the whole interface.

Why it matters:
- Sovereignty depends on owning the state layer, not just swapping in a local model.
- Shared state lets later-generated tools integrate into an existing environment instead of creating another silo.
- A personal context bus is a cleaner foundation for local-first agents than stuffing more context into one giant prompt window.

How it fits into strategy:
- Local-first layer: user state should live in a durable substrate the user controls.
- Operating-system layer: chat becomes one interface over personal state, not the container for all state.
- Memory layer: durable artifacts, write-back affordances, and scoped shared context are more governable than transcript-centric memory.

What is implementable now:
- introduce a local event or state bus that tools can publish to and subscribe from
- model shared artifacts explicitly with typed schemas and ownership metadata
- expose write-back operations as governed capabilities instead of free-form chat side effects
- treat chat as a view over shared state, not as the state store itself

What remains conceptual:
- the paper is based on a limited autobiographical deployment, not broad production evidence
- interoperability standards for personal context buses are still immature
- shared state increases the need for policy, provenance, and conflict resolution around writes

Practical tools, repos, and methodologies worth exploring:
- local SQLite or event-log-backed state stores
- pub/sub or event-bus patterns for personal tools
- typed artifact registries with explicit ownership and scope
- audit logs for write-back actions across chat and GUI surfaces

Opinionated take:
Most personal agents are not failing because the model is too weak. They are failing because there is no coherent state substrate for the rest of the system to stand on.

Implementability score: 0.57

## Strategic take
The sovereignty story is getting sharper. Defensive posture has to be tested against adaptive injection, and local-first ambition has to include ownership of the shared state layer. Otherwise the system is either easy to subvert or too fragmented to matter.
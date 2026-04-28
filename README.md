# Eliezer Weekly Roundup

A living, category-first research system for the agentic stack: agents, tools, memory, orchestration, evaluation, local-first infrastructure, and strategy.

The primary lens is the agentic stack itself, not generic AI news. The repo tracks research and releases that change how a builder should design autonomous systems: orchestration, prompting, tool use, memory, deterministic testing, observability, multi-agent systems, model routing, and sovereign or self-hosted infrastructure.

## Latest update

- Daily scan 2026-04-28: [daily synthesis](roundups/2026-04-28.md)
- AgenticAI analysis: [2026-04-28](AgenticAI/2026-04-28/reasoning.md)
- Strategy analysis: [2026-04-28](Strategy/2026-04-28/sovereignty.md)
- Fresh AgenticAI index: [AgenticAI README](AgenticAI/README.md)
- Fresh Strategy index: [Strategy README](Strategy/README.md)
- Prior Friday synthesis: [week ending 2026-04-24](roundups/2026-04-24.md)

## Current thesis

- Coding-agent orchestration is moving from interactive sessions to ticket-native control planes: issue trackers, isolated workspaces, workflow contracts, and proof-of-work artifacts.
- Agent selection is becoming a retrieval-and-evaluation problem: descriptions are weak signals, while execution traces, probes, and task-level outcomes are stronger routing evidence.
- Agent memory is moving away from vector-only transcript recall toward typed, versioned, conflict-aware state that can be audited and updated.
- Agent runtimes are becoming replayable systems: checkpoints, forks, resumable sessions, lifecycle events, sandbox substrates, and stream-preserving traces are now core primitives.
- Skills and grounding documents are becoming installable control packages, but large skill libraries need retrieval gates and machine-readable execution/risk structure.
- Boundary safety must live below the prompt: lifecycle governance, semantic tool-call mediation, local PII filtering, portable permissions, sandboxed execution, and evidence traces.
- The agent stack is moving from context maximalism to context operations: tool schemas, code, memory, traces, KV cache, skills, and recursive inspection all need admission control.
- Sovereignty is becoming local context infrastructure plus router governance: what stays on-device, what escalates, what is indexed locally, and what passes through provider gateways all need explicit policy.

## Browse by category

- [AgenticAI](AgenticAI/README.md): implementation-focused analysis on runtimes, evals, memory, tooling, and environment design.
- [Strategy](Strategy/README.md): strategic analysis on sovereignty, governance, infrastructure, operating models, and enterprise adoption.

## Durable topics

- [Ticket-Native Agent Orchestration](AgenticAI/ticket-native-agent-orchestration/ticket-native-agent-orchestration.md)
- [Agent Discovery](AgenticAI/agent-discovery/agent-discovery.md)
- [Skills as Control](AgenticAI/skills-as-control/skills-as-control.md)
- [Trajectory-Aware Evaluation](AgenticAI/trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Context Economy for Agents](AgenticAI/context-economy/context-economy.md)
- [Memory Systems](AgenticAI/memory-systems/memory-systems.md)
- [Local-First Agents](Strategy/local-first-agents/local-first-agents.md)
- [Agent Sandboxing](Strategy/agent-sandboxing/agent-sandboxing.md)
- [Runtime Governance](Strategy/runtime-governance/runtime-governance.md)
- [Model Router Governance](Strategy/model-router-governance/model-router-governance.md)

## How the repo is organized

- `AgenticAI/YYYY-MM-DD/reasoning.md`: category analysis for the week or day, with source links and implementation guidance.
- `Strategy/YYYY-MM-DD/sovereignty.md`: strategy analysis for the week or day, with source links and implementation guidance.
- `AgenticAI/<topic>/<topic>.md` and `Strategy/<topic>/<topic>.md`: durable deep dives when a pattern deserves to persist beyond one cycle.
- `roundups/YYYY-MM-DD.md`: cross-category synthesis tying implementable patterns to strategic implications.

## What gets selected

Selected items usually have at least one of these properties:

- they change agent orchestration, tool use, memory, or evaluation practice;
- they expose a repeatable implementation pattern that can be tried now;
- they show where local-first or self-hosted infrastructure is becoming practical;
- they reveal a governance, containment, or observability requirement that serious agent builders should design around;
- they clarify model-routing and reasoning tradeoffs rather than merely announcing a bigger model.

## Implementability scores

- `1.0`: straightforward to implement now with standard tools and normal engineering effort.
- `0.5`: implementable, but it needs meaningful architecture or operational sophistication.
- `0.0`: mostly conceptual, speculative, or blocked on missing research or infrastructure.

## Subscribe

Use GitHub's Watch feature if you want repo updates as the research system evolves. The category READMEs are the intended entry points; the roundup is the synthesis layer.

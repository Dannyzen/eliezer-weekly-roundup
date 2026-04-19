# Eliezer Weekly Roundup

A category-first research repo for tracking what matters in agentic AI and strategy each week.

## Latest week
- Week ending 2026-04-19: [Daily scan](roundups/2026-04-19.md)
- Fresh AgenticAI signal: [current implementation signal](AgenticAI/README.md)
- Fresh Strategy signal: [current sovereignty and governance signal](Strategy/README.md)
- Durable topic to revisit: [Trajectory-Aware Evaluation](AgenticAI/trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- Durable strategy topic to revisit: [Local-First Agents](Strategy/local-first-agents/local-first-agents.md)

## Current signal
- Workflow serving is becoming its own systems problem; multi-LLM agent stacks need allocation policies that optimize the whole workflow, not each model in isolation.
- Blind prompt optimization in compound systems is mostly wasted motion unless the task has real structural headroom.
- Open agent frameworks are converging on the same operator surface: delegation via tool calls, local execution, skills, and traceable observers.
- Sovereign or local-first AI increasingly depends on explicit escalation policy: keep easy or sensitive work local, then hotswap only the failing trajectories.

## Browse by category
- [AgenticAI](AgenticAI/README.md)
- [Strategy](Strategy/README.md)

## How the repo is organized
- `AgenticAI/YYYY-MM-DD/reasoning.md`: implementation-focused analysis on runtimes, evals, memory, tooling, and environment design.
- `Strategy/YYYY-MM-DD/sovereignty.md`: strategic analysis on governance, sovereign infrastructure, local-first systems, operating models, and enterprise adoption.
- `AgenticAI/<topic>/<topic>.md` and `Strategy/<topic>/<topic>.md`: durable deep dives when a pattern deserves to persist beyond one cycle.
- `roundups/YYYY-MM-DD.md`: weekly synthesis or daily scan tying both categories into one opinionated model.

## How to read it
1. Start with a category README for the current week's strongest findings.
2. Jump into the dated analysis file for the detailed argument, sources, and implementation guidance.
3. Use durable topic pages when a theme keeps compounding across weeks.
4. Use the roundup when you want the cross-category view of what is implementable now versus what is still architecture-heavy.

## Implementability scores
- `1.0`: straightforward to implement now with standard tools and normal engineering effort
- `0.5`: implementable, but it needs meaningful architecture or operational sophistication
- `0.0`: mostly conceptual, speculative, or blocked on missing research or infrastructure

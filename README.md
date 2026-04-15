# Eliezer Weekly Roundup

A category-first research repo for tracking what matters in agentic AI and strategy each week.

## Latest week
- Week of 2026-04-13: [Wednesday daily scan](roundups/2026-04-15.md)
- AgenticAI index: [current implementation signal](AgenticAI/README.md)
- Strategy index: [current sovereignty and governance signal](Strategy/README.md)
- Deep dive to revisit: [File-as-Bus Workspaces](AgenticAI/file-as-bus-workspaces/file-as-bus-workspaces.md)
- Durable memory topic to revisit: [Memory Systems](AgenticAI/memory-systems/memory-systems.md)

## Current signal
- Long-horizon agents need durable workspace state more than longer chat handoffs.
- Cross-session memory gets better when facts keep contextual scene traces.
- Installable memory infrastructure is more useful than hidden context stuffing.
- Model routing only becomes real when it optimizes multi-turn trajectories.
- No separate strategy note was strong enough to justify a fresh category update today.

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
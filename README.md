# Eliezer Weekly Roundup

A category-first research repo for tracking what matters in agentic AI and strategy each week.

## Latest week
- Week of 2026-04-13: [Monday daily scan](roundups/2026-04-13.md)
- AgenticAI index: [current implementation signal](AgenticAI/README.md)
- Strategy index: [current sovereignty and governance signal](Strategy/README.md)
- Deep dive to revisit: [Memory Systems](AgenticAI/memory-systems/memory-systems.md)
- Durable governance topic to revisit: [Runtime Governance](Strategy/runtime-governance/runtime-governance.md)

## Current signal
- Managed agents are becoming workflow-native instead of prompt-native.
- Memory systems are becoming installable, inspectable operator infrastructure.
- Checkpoint restore paths are becoming part of the runtime threat model.
- Better agent evaluation is starting to score whether the system knew to ask for help.

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

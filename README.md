# Eliezer Weekly Roundup

A category-first research repo for tracking what matters in agentic AI and strategy each week.

## Latest week
- Week of 2026-04-13: [Tuesday daily scan](roundups/2026-04-14.md)
- AgenticAI index: [current implementation signal](AgenticAI/README.md)
- Strategy index: [current sovereignty and governance signal](Strategy/README.md)
- Deep dive to revisit: [Trajectory-Aware Evaluation](AgenticAI/trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- Durable governance topic to revisit: [Governed Workflow Substrates](Strategy/governed-workflow-substrates/governed-workflow-substrates.md)

## Current signal
- Portable skill stacks are becoming a cross-runtime agent operating system.
- Tool-use work is converging on common traces and evaluation surfaces.
- Coding agents need compressed reasoning state, not transcript hoarding.
- Agent debugging is moving toward trace trees and failure-onset localization.
- Infrastructure vendors are packaging the runtime substrate for long-lived agents.

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

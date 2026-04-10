# Eliezer Weekly Roundup

A category-first research repo for tracking what matters in agentic AI and strategy each week.

## Latest week
- Week of 2026-04-10: [full synthesis](roundups/2026-04-10.md)
- Deep Dive Wednesday winner: [Governed Workflow Substrates](Strategy/governed-workflow-substrates/governed-workflow-substrates.md)
- New durable topic this week: [Shared-State Agents](Strategy/shared-state-agents/shared-state-agents.md)

## Current signal
- Runtime and UI contracts are becoming more explicit, which is what makes orchestration testable instead of magical.
- Honest agent evaluation is moving onto live sites with safe side-effect interception instead of toy browser sandboxes.
- Prompt injection defense still collapses under broader and more adaptive evaluation than most vendors advertise.
- Sovereign personal agents need owned shared state, not just a local model and a chat box.

## Browse by category
- [AgenticAI](AgenticAI/README.md)
- [Strategy](Strategy/README.md)

## Structure
- `AgenticAI/YYYY-MM-DD/reasoning.md`: implementation-focused research on agent systems, orchestration, evals, memory, and tooling.
- `Strategy/YYYY-MM-DD/sovereignty.md`: strategic analysis on sovereign infrastructure, governance, operating models, and enterprise adoption.
- `AgenticAI/<topic>/<topic>.md` and `Strategy/<topic>/<topic>.md`: durable topic pages when a pattern deserves to persist beyond one day.
- `roundups/YYYY-MM-DD.md`: daily or weekly synthesis across both categories.

## How to use this repo
1. Start with a category README for the current week's signal.
2. Jump into the dated analysis file for full explanation and source grounding.
3. Use durable topic pages when a pattern clearly matters beyond one cycle.
4. Use the roundup for the cross-category model of what is implementable now versus what still needs architecture work.

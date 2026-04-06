# Eliezer Weekly Roundup

A category-first research repo for tracking what matters in agentic AI and strategy each week.

## Latest week
- Week of 2026-04-05: [full synthesis](roundups/2026-04-05.md)

## Current signal
- Agent frameworks are getting stable enough to standardize around, not just experiment with.
- The strongest practical gains are coming from runtime discipline: prompt caching, thread executors, trajectory triage, and policy enforcement.
- Memory is becoming a security boundary. If it is persistent, it needs the same defensive posture as tools and credentials.

## Browse by category
- [AgenticAI](AgenticAI/README.md)
- [Strategy](Strategy/README.md)

## Structure
- `AgenticAI/YYYY-MM-DD/reasoning.md`: implementation-focused research on agent systems, orchestration, evals, memory, and tooling.
- `Strategy/YYYY-MM-DD/sovereignty.md`: strategic analysis on sovereign infrastructure, governance, operating models, and enterprise adoption.
- `AgenticAI/<topic>/<topic>.md` and `Strategy/<topic>/<topic>.md`: durable topic pages when a finding deserves to persist beyond one day.
- `roundups/YYYY-MM-DD.md`: daily or weekly synthesis across both categories.

## How to use this repo
1. Start with a category README for the current week's signal.
2. Jump into the dated analysis file for full explanation and source grounding.
3. Use durable topic pages when a pattern clearly matters beyond one cycle.
4. Use the roundup for the cross-category model of what is implementable now versus what still needs architecture work.

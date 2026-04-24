# Eliezer Weekly Roundup

A category-first research repo for tracking what matters in agentic AI and strategy each week.

## Latest week
- Week ending 2026-04-24: [Daily scan](roundups/2026-04-24.md)
- Fresh AgenticAI signal: [current implementation signal](AgenticAI/README.md)
- Fresh Strategy signal: [current sovereignty and infrastructure signal](Strategy/README.md)
- Durable topic to revisit: [Context Economy for Agents](AgenticAI/context-economy/context-economy.md)
- Durable strategy topic to revisit: [Local-First Agents](Strategy/local-first-agents/local-first-agents.md)

## Current signal
- Agent builders are moving from context maximalism to context accounting: KV-cache economics, tool-schema gating, code-context retrieval, and structured memory all matter.
- DeepSeek-V4 is a useful long-context agent signal because it treats KV cache, tool-call schema, interleaved reasoning, and sandbox RL as one system.
- MCP and repository context need admission control; `zilliztech/claude-context` is the most worth-trying GitHub-trending tool today.
- Agent memory needs event structure, temporal anchors, and background consolidation, not just isolated vectorized facts.
- Cloud infrastructure is splitting between training and low-latency agentic serving; that is useful bottleneck evidence and a portability warning.

## Browse by category
- [AgenticAI](AgenticAI/README.md)
- [Strategy](Strategy/README.md)

## How the repo is organized
- `AgenticAI/YYYY-MM-DD/reasoning.md`: implementation-focused analysis on runtimes, evals, memory, tooling, and environment design.
- `Strategy/YYYY-MM-DD/sovereignty.md`: strategic analysis on governance, sovereign infrastructure, local-first systems, operating models, and enterprise adoption.
- `AgenticAI/<topic>/<topic>.md` and `Strategy/<topic>/<topic>.md`: durable deep dives when a pattern deserves to persist beyond one cycle.
- `roundups/YYYY-MM-DD.md`: weekly synthesis or daily scan tying both categories into one opinionated model.

## NotebookLM podcast MVP
1. Install project dependencies with `uv sync`.
2. Install Chromium for the first NotebookLM login with `uv run playwright install chromium`.
3. Authenticate NotebookLM once with `uv run notebooklm login`.
4. Generate or reuse a report notebook and podcast:
   - `uv run eliezer-roundup generate-podcast roundups/2026-04-24.md`
   - add `--push` if you want the updated markdown, podcast file, and manifest committed and pushed to GitHub.

What the command does:
- creates or reuses one NotebookLM notebook per report title
- uploads the report markdown content plus cited URLs as NotebookLM sources
- generates an audio overview and downloads it next to the report markdown, for example `roundups/2026-04-24.notebooklm.mp3`
- updates the markdown with a managed `## Audio Overview` section linking to the podcast
- writes durable notebook and artifact ids to `.notebooklm-sync.json`

## How to read it
1. Start with a category README for the current week's strongest findings.
2. Jump into the dated analysis file for the detailed argument, sources, and implementation guidance.
3. Use durable topic pages when a theme keeps compounding across weeks.
4. Use the roundup when you want the cross-category view of what is implementable now versus what is still architecture-heavy.

## Implementability scores
- `1.0`: straightforward to implement now with standard tools and normal engineering effort
- `0.5`: implementable, but it needs meaningful architecture or operational sophistication
- `0.0`: mostly conceptual, speculative, or blocked on missing research or infrastructure

# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-04-27

### Local-first code and task context is becoming the sovereign coding-agent substrate
Summary: GitHub Trending surfaced two practical local-first context systems: GitNexus indexes code into a local knowledge graph and exposes it through CLI/MCP, while Beads gives coding agents a Dolt-backed graph issue tracker with dependency, task, and message memory. The strategic move is clear: keep repository structure, task state, and agent coordination data close to the operator before escalating to hosted models.

Analysis: [sovereignty analysis](2026-04-27/sovereignty.md#local-first-code-and-task-context-is-becoming-the-sovereign-coding-agent-substrate)
Durable topic: [Local-First Agents](local-first-agents/local-first-agents.md)
Core source: [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
Supporting sources:
- [GitNexus v1.6.4-rc.9](https://github.com/abhigyanpatwari/GitNexus/releases/tag/v1.6.4-rc.9)
- [Beads](https://github.com/gastownhall/beads)
- [Beads v1.0.3](https://github.com/gastownhall/beads/releases/tag/v1.0.3)
Implementable now:
- index repositories locally and expose code-graph context through MCP rather than uploading whole repos to hosted tools
- keep agent task memory in a structured dependency graph instead of markdown scratchpads
- use GitNexus or similar local code context tools for blast-radius and dependency-aware edits
- use Beads-style task graphs for multi-agent handoffs, claims, blockers, and audit trails
Tools, repos, and methodologies worth exploring:
- GitNexus CLI/MCP and bridge mode
- Beads `bd` CLI, Dolt-backed task graph, JSON schema envelope, and gates
- local-first code graph indexing
- checksum verification and license review before production adoption
Implementability score: 0.86

# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-14

### Portable skill stacks are becoming a cross-runtime agent operating system
Summary: The clearest implementation signal today is that agent procedure is becoming portable. Skills, plans, review loops, and subagent workflows are being packaged so they can move across runtimes instead of living inside one vendor's chat UX.

Analysis: [reasoning analysis](2026-04-14/reasoning.md#portable-skill-stacks-are-becoming-a-cross-runtime-agent-operating-system)
Core source: [Superpowers](https://github.com/obra/superpowers)
Implementable now:
- package recurring agent workflows as explicit skills or playbooks
- require plan, test, review, and finish phases rather than relying on vibes
- keep agent methodology portable enough to survive model or vendor swaps
- version workflow logic the way you would version any other critical operational artifact
Tools, repos, and methodologies worth exploring:
- [Superpowers](https://github.com/obra/superpowers)
- portable skill registries
- subagent-driven development
- TDD-first agent workflows
- plugin-based runtime portability
Implementability score: 0.96

### Tool-use is finally getting a common representation and eval surface
Summary: The most useful paper signal today is not a bigger tool benchmark score. It is an attempt to standardize the grammar of tool use so datasets, traces, and evaluations stop talking past each other.

Analysis: [reasoning analysis](2026-04-14/reasoning.md#tool-use-is-finally-getting-a-common-representation-and-eval-surface)
Core source: [UniToolCall](https://arxiv.org/abs/2604.11557)
Implementable now:
- normalize internal traces into a query-action-observation-answer structure
- score tool use at function, turn, and conversation levels
- generate eval cases for serial versus parallel and single-turn versus multi-turn patterns
- preserve cross-turn anchors when early tool results should constrain later actions
Tools, repos, and methodologies worth exploring:
- [UniToolCall](https://arxiv.org/abs/2604.11557)
- QAOA-style event schemas
- structurally balanced tool-call datasets
- distractor-heavy tool selection tests
- multi-level tool-use scoring
Implementability score: 0.89

### Dynamic reasoning context is replacing transcript hoarding in coding agents
Summary: The best coding-agent pattern today is explicit reasoning-state management. Keep recent reasoning live, compress older reasoning into digests, and stop pretending the full transcript belongs in the prompt forever.

Analysis: [reasoning analysis](2026-04-14/reasoning.md#dynamic-reasoning-context-is-replacing-transcript-hoarding-in-coding-agents)
Core source: [SWE-AGILE](https://arxiv.org/abs/2604.11716)
Implementable now:
- maintain a short live window of detailed reasoning and compress older state into digests
- summarize by decision and dependency instead of generic prose
- rehydrate only the digests relevant to the current subproblem
- measure context policy by redundant work avoided as well as token savings
Tools, repos, and methodologies worth exploring:
- [SWE-AGILE](https://arxiv.org/abs/2604.11716)
- sliding-window reasoning buffers
- digest-based context compaction
- dependency-aware summary generation
- SWE-Bench-style long-horizon task analysis
Implementability score: 0.86

### Trace trees are becoming the debugging primitive for code agents
Summary: Flat transcripts are not enough for serious agent debugging. The stronger pattern is reconstructing stage and step hierarchies so teams can identify the first bad move and the failure chain it created.

Analysis: [reasoning analysis](2026-04-14/reasoning.md#trace-trees-are-becoming-the-debugging-primitive-for-code-agents)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [CodeTracer](https://arxiv.org/abs/2604.11641)
Implementable now:
- emit structured state-transition events instead of only chat logs
- reconstruct failures into stage and step hierarchies
- tag likely first-failure points separately from downstream effects
- feed diagnostics into controlled replay or repair loops
Tools, repos, and methodologies worth exploring:
- [CodeTracer](https://arxiv.org/abs/2604.11641)
- trace-tree reconstruction
- failure onset localization
- replay-assisted recovery
- stage-level and step-level debugging
Implementability score: 0.79

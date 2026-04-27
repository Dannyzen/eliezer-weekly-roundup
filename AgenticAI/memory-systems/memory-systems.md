# Memory Systems

Memory is becoming the real architecture question for long-lived agents.

The durable pattern across recent work is simple: agents become more useful when memory preserves ground truth, retrieves broader context than a single chunk, and distinguishes between what should stay local, what should become durable profile data, and what should remain ephemeral. The new wrinkle is that the best systems are no longer treating memory as transcript storage. They are turning experience into portable guidance and giving operators much better control over what gets written and recalled.

## Why this topic now

The April 2026 wave of memory work is pushing seven ideas into focus:
- **MemMachine** argues that episodic memory should preserve full conversational evidence rather than summarize too aggressively.
- **FileGram** argues that personalization should be grounded in behavioral traces from local file activity, not just dialogue.
- **Springdrift** argues that persistent memory must be embedded in an auditable runtime with explicit recovery and policy controls.
- **ALTK-Evolve** argues that the real goal is not replaying transcripts but extracting reusable guidelines, policies, and SOPs from trajectories.
- **Drawing on Memory** argues that durable facts should be paired with contextual scene traces so temporal reasoning and update tracking survive across sessions.
- **claude-mem** shows that installable memory infrastructure with search, citations, and progressive disclosure is a more practical product shape than hidden context injection.
- **Memory Transfer Learning** shows that memory becomes much more valuable when distilled lessons transfer across domains instead of staying trapped inside one benchmark.
- **StructMem** argues that long-horizon memory needs event-level bindings, temporal anchors, and cross-event links rather than isolated vectorized facts.

Core sources:
- MemMachine: https://arxiv.org/abs/2604.04853
- FileGram: https://arxiv.org/abs/2604.04901
- Springdrift: https://arxiv.org/abs/2604.04660
- ALTK-Evolve article: https://huggingface.co/blog/ibm-research/altk-evolve
- ALTK-Evolve paper: https://arxiv.org/abs/2603.10600
- Drawing on Memory: https://arxiv.org/abs/2604.12948
- claude-mem: https://github.com/thedotmack/claude-mem
- Memory Transfer Learning: https://arxiv.org/abs/2604.14004
- Experience Compression Spectrum: https://arxiv.org/abs/2604.15877
- StructMem: https://arxiv.org/abs/2604.21748
- LightMem: https://github.com/zjunlp/LightMem

## Core thesis

The wrong question is "how do we give the agent more memory?"

The right questions are:
- what evidence should be preserved verbatim?
- what can be compressed safely?
- what should become a reusable guideline?
- what should remain local?
- what contextual trace should travel with a stored fact?
- how should retrieval adapt to the query?
- what policy should govern writes, reads, and profile formation?
- what abstraction level makes a memory transferable to new tasks?

If those questions are ignored, memory turns into a lossy, leaky mess that is simultaneously unhelpful and unsafe.

## The three memory layers that matter

### 1. Episodic memory
This is the raw record of what happened: conversations, tool calls, outcomes, and surrounding context.

Current lesson:
- preserve more of the original episode than most systems do today
- index it intelligently, but do not treat aggressive extraction as truth preservation
- keep enough context to reconstruct why a fact was learned, not just the fact itself

### 2. Profile memory
This is the durable model of the user, workflow, project, and preferences.

Current lesson:
- build profile memory from repeated evidence, not one-off statements
- distinguish stable traits from transient task state
- keep especially sensitive profile signals local by default

### 3. Procedural memory
This is how the system remembers how to act: routines, playbooks, policies, and recovery paths.

Current lesson:
- some of the most important memory is operational, not conversational
- if the runtime cannot recover, replay, and justify decisions, the memory system is incomplete
- the most useful promoted memories often look like guidelines, not transcripts

## What to build now

### Preserve raw episodes
Store the full interaction episode plus metadata, then layer indexing and summarization on top. Do not throw away ground truth during ingestion.

### Retrieve neighborhoods, not just chunks
When one relevant turn is found, expand around it. Adjacent actions and context often matter more than the isolated snippet that matched the query.

### Separate trust tiers
Not every memory object deserves the same scope.

Use at least three tiers:
- ephemeral working memory
- durable but local profile memory
- externally shareable or system-wide memory

### Put policy on memory writes
Treat memory writes as consequential actions. Some memories change future behavior and should pass policy checks or confidence thresholds before becoming durable.

### Distill guidelines, not just summaries
Run offline passes that convert repeated trajectory patterns into concise guidelines, policies, and SOPs. Retrieval should surface those distilled lessons when they matter instead of dragging whole transcripts back into the prompt.

### Store contextual traces with durable facts
A durable memory entry should not be only a proposition. Pair it with a lightweight scene trace: where it came from, when it was learned, and what local situation made it relevant.

### Promote memories at the abstraction level that transfers
Raw traces are useful for audit and close-match replay, but cross-domain reuse depends on extracting higher-level workflows, validation routines, and generalizable insights.

### Measure memory by continuity, transfer, and reversibility
Useful metrics include:
- factual continuity across sessions
- profile accuracy over time
- retrieval precision under noisy histories
- token efficiency for grounded recall
- reversibility and auditability of memory changes
- transfer gain from retrieved guidelines on unseen tasks
- temporal reasoning and update-tracking accuracy

## What to avoid

Avoid these traps:
- turning every conversation into a flattened summary
- treating vector search alone as a memory architecture
- mixing user profile, task scratchpad, and governance history into one blob
- letting behavioral traces flow into permanent memory without clear consent or scope
- assuming bigger context windows remove the need for memory design
- confusing transcript replay with actual learning
- writing decontextualized facts and hoping retrieval can recover the missing situation later
- promoting overly specific low-level traces as if they will transfer cleanly to new task domains

## New April 2026 additions

### Typed semantic memory is the practical middle path after vector-only and graph-heavy memory
Memanto sharpens the memory architecture tradeoff. The paper argues that high-fidelity agent memory does not always require LLM-mediated entity extraction, explicit graph schema maintenance, and multi-query retrieval. Its proposed pattern is typed semantic memory, automated conflict resolution, temporal versioning, and a single-query retrieval path.

The immediate design lesson is not to depend blindly on one proprietary retrieval backend. It is to make memory writes more disciplined:
- classify durable memories into typed categories;
- attach timestamp, source, supersession, and conflict metadata;
- reconcile contradictions at write time instead of asking the answerer to improvise later;
- keep the online retrieval path cheap enough to use continuously;
- evaluate long-horizon continuity with realistic temporal and multi-session tasks.

This connects directly to StructMem and WorldDB. Flat memory is too lossy, but full graph memory can be expensive and brittle. A typed, versioned event/state layer is the practical middle path for many agent products.

Source:
- [Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents](https://arxiv.org/abs/2604.22085)

### Memory, skills, and rules are one compression pipeline
Experience Compression Spectrum adds the abstraction this category was missing. Episodic memory, procedural skills, and declarative rules are not separate product features. They are compression levels for the same underlying experience. The practical move is to preserve evidence once, then promote it along a governed ladder from episode to reusable routine to compact rule when transfer value is high and specificity costs are acceptable. The paper's "missing diagonal" is the opportunity: most systems can store or summarize, but very few can adapt compression level to the query, the time horizon, or the privacy tier.

The concrete design hint is useful immediately. Treat memory promotion as a lifecycle problem with three explicit targets:
- episodic recall when auditability and context fidelity matter
- skill extraction when a reusable procedure keeps paying off
- rule distillation when the lesson is stable enough to survive aggressive compression

The compression ratios in the paper make the trade-off legible instead of mystical: roughly 5-20x for episodic memory, 50-500x for skills, and 1,000x or more for rules. That is the right language for designing memory budgets.

### Cross-domain transfer favors insight over trace replay
Memory Transfer Learning sharpens the promotion problem. The memory object that transfers best is usually not the full episode and not even the task-specific summary. It is the reusable insight: validation habits, safe-editing routines, workflow constraints, and debugging patterns that survive a change of benchmark.

### Searchable memory compression is becoming installable infrastructure
`claude-mem` is useful signal because it turns persistent memory into a product surface an operator can actually use: one-command install, searchable observations, progressive disclosure, explicit privacy exclusions, and inspectable citations. That pushes memory architecture in the right direction. Durable context should behave like governed infrastructure, not hidden prompt residue.

### Dual-trace encoding fixes the weakest part of flat memory
Drawing on Memory makes the strongest recent empirical case that a fact should travel with a scene trace. That extra encoding pressure improves the kinds of recall that agents actually fail at in the wild: temporal reasoning, update tracking, and multi-session aggregation.

### Guidelines beat transcripts when the goal is transfer
ALTK-Evolve sharpens the practical memory lesson of the month: the agent should not keep relearning from raw logs every time. Good memory systems preserve the episode, then promote the parts that proved reusable. That makes memory smaller, more auditable, and more transferable.

### Memory quality loops belong off the critical path
The most robust pattern is a two-loop design: the online loop acts, while a background consolidation loop scores, merges, and prunes learned guidance. That keeps the action path lean without giving up long-term improvement.

### Write-time reconciliation is the next memory moat
WorldDB adds an important correction to current memory fashion. The problem is not only retrieving the right fact. It is deciding what a new write should do to the memory state. Flat vector stores and many graph memories still treat updates as passive additions, then hope the answerer can reconcile contradictions later. WorldDB argues for the opposite design: nodes should be immutable and content-addressed, while edge types should execute write-time behavior such as supersession, contradiction handling, and merge proposals.

That matters because many of the failures operators actually care about are state failures, not retrieval failures:
- stale preferences that should have been replaced
- conflicting facts that should have remained visible as conflicts
- aliases that should have been merged earlier
- audit trails that vanish once summaries overwrite the past

The practical lesson is immediate even if the full architecture is heavy. High-value memory should stop behaving like an append-only note pad. It should have explicit mutation semantics, version lineage, and enough structure that update tracking does not depend on whatever the answering model improvises at query time.

### StructMem makes event structure the practical middle path between flat memory and brittle graphs
StructMem adds a useful correction to the memory stack. Flat memory is cheap, but it loses the relations that matter for long-horizon behavior. Full graph memory can model relationships, but construction and maintenance are expensive and fragile. StructMem sits in the middle: preserve event-level bindings, temporally anchor memories, induce cross-event links, and periodically consolidate related items in the background.

The implementation lesson is direct:
- store memory as events with provenance, timestamps, participants, and relation candidates
- retrieve event neighborhoods rather than isolated nearest-neighbor chunks
- run consolidation off the critical path so the online loop stays fast
- evaluate memory on temporal and multi-hop behavior, not just fact recall

Source:
- [StructMem: Structured Memory for Long-Horizon Behavior in LLMs](https://arxiv.org/abs/2604.21748)
- [zjunlp/LightMem](https://github.com/zjunlp/LightMem)

## Working conclusion

The next generation of agents will be differentiated less by how eloquently they speak and more by how faithfully they remember. The winning systems will preserve evidence, retrieve context adaptively, promote only the right lessons into durable guidance, attach enough context for updates and temporal reasoning, choose abstraction levels that transfer across tasks, and keep the most sensitive memory close to the user and under policy control.

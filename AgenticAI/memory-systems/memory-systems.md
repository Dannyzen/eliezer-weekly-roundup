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

Core sources:
- MemMachine: https://arxiv.org/abs/2604.04853
- FileGram: https://arxiv.org/abs/2604.04901
- Springdrift: https://arxiv.org/abs/2604.04660
- ALTK-Evolve article: https://huggingface.co/blog/ibm-research/altk-evolve
- ALTK-Evolve paper: https://arxiv.org/abs/2603.10600
- Drawing on Memory: https://arxiv.org/abs/2604.12948
- claude-mem: https://github.com/thedotmack/claude-mem
- Memory Transfer Learning: https://arxiv.org/abs/2604.14004

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

## Working conclusion

The next generation of agents will be differentiated less by how eloquently they speak and more by how faithfully they remember. The winning systems will preserve evidence, retrieve context adaptively, promote only the right lessons into durable guidance, attach enough context for updates and temporal reasoning, choose abstraction levels that transfer across tasks, and keep the most sensitive memory close to the user and under policy control.

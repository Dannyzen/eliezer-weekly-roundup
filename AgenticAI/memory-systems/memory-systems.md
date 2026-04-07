# Memory Systems

Memory is becoming the real architecture question for long-lived agents.

The durable pattern across recent work is simple: agents become more useful when memory preserves ground truth, retrieves broader context than a single chunk, and distinguishes between what should stay local, what should become durable profile data, and what should remain ephemeral.

## Why this topic now

The April 2026 wave of memory work is pushing three ideas into focus:
- **MemMachine** argues that episodic memory should preserve full conversational evidence rather than summarize too aggressively.
- **FileGram** argues that personalization should be grounded in behavioral traces from local file activity, not just dialogue.
- **Springdrift** argues that persistent memory must be embedded in an auditable runtime with explicit recovery and policy controls.

Core sources:
- MemMachine: https://arxiv.org/abs/2604.04853
- FileGram: https://arxiv.org/abs/2604.04901
- Springdrift: https://arxiv.org/abs/2604.04660

## Core thesis

The wrong question is "how do we give the agent more memory?"

The right questions are:
- what evidence should be preserved verbatim?
- what can be compressed safely?
- what should remain local?
- how should retrieval adapt to the query?
- what policy should govern writes, reads, and profile formation?

If those questions are ignored, memory turns into a lossy, leaky mess that is simultaneously unhelpful and unsafe.

## The three memory layers that matter

### 1. Episodic memory
This is the raw record of what happened: conversations, tool calls, outcomes, and surrounding context.

Current lesson:
- preserve more of the original episode than most systems do today
- index it intelligently, but do not treat aggressive extraction as truth preservation

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

### Measure memory by continuity, not vibes
Useful metrics include:
- factual continuity across sessions
- profile accuracy over time
- retrieval precision under noisy histories
- token efficiency for grounded recall
- reversibility and auditability of memory changes

## What to avoid

Avoid these traps:
- turning every conversation into a flattened summary
- treating vector search alone as a memory architecture
- mixing user profile, task scratchpad, and governance history into one blob
- letting behavioral traces flow into permanent memory without clear consent or scope
- assuming bigger context windows remove the need for memory design

## Working conclusion

The next generation of agents will be differentiated less by how eloquently they speak and more by how faithfully they remember. The winning systems will preserve evidence, retrieve context adaptively, and keep the most sensitive memory close to the user and under policy control.

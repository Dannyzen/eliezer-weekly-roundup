# File-as-Bus Workspaces

File-as-Bus is the most practical design pattern I have seen this week for long-horizon agent work.

The core idea is simple: agents should coordinate through durable project artifacts instead of relying primarily on conversational handoff. Plans, analyses, code, experiment logs, and decision summaries become the shared medium. The orchestrator stays thin and stage-aware. Specialists repeatedly re-ground on the same workspace state.

## Why this topic matters

Long-running agents usually fail for boring reasons:
- conversational context drifts
- one subagent invents a local plan that never becomes durable
- later steps cannot tell which artifact is authoritative
- verification happens against stale assumptions rather than current project state

File-as-Bus fixes that by making the workspace itself the communication substrate.

## Core source

- AiScientist paper: https://arxiv.org/abs/2604.13018
- AiScientist repo: https://github.com/AweAI-Team/AiScientist

## Core thesis

Thin control over thick state is the right default for long-horizon agents.

The orchestrator should own:
- stage progression
- delegation boundaries
- concise summaries
- workspace map updates
- verification gates

The specialists should own:
- producing or editing bounded artifacts
- re-grounding on existing files before acting
- leaving durable outputs instead of conversational residue

## What the pattern looks like

### 1. Shared workspace map
Maintain a small durable index answering:
- what artifacts exist
- which ones are authoritative
- what stage the project is in
- which agents can touch which files
- what still needs verification

### 2. Artifact-first delegation
Delegation should name inputs and outputs explicitly.

Bad delegation:
- "continue where we left off"

Better delegation:
- read `plan.md`, `results/ablation-a.md`, and `src/runner.py`
- update `results/ablation-b.md`
- do not modify `plan.md`
- return a short summary of what changed and what failed

### 3. Thin summaries
The orchestrator should not carry giant narrative state. It should keep:
- stage summary
- current blockers
- artifact map
- next verification target

Everything else belongs in files.

### 4. Permission-scoped edits
Parallel agents become much safer when edit authority is explicit.

At minimum distinguish:
- read-only reference artifacts
- writable work products
- controlled summary files updated only by the coordinator

### 5. Verification against artifacts
Verification should check actual workspace state:
- do the expected files exist
- do outputs match the stated stage goal
- did tests or experiments run
- are summaries consistent with artifacts

## Why it fits the agentic stack

- **Orchestration:** stage control becomes cleaner when the coordinator manages artifact flow rather than chat flow.
- **Memory:** the workspace is durable external memory with clear scope and provenance.
- **Observability:** file histories are easier to inspect and replay than sprawling conversations.
- **Multi-agent safety:** artifact boundaries reduce silent overwrite and hidden divergence.

## What to build now

- keep a `workspace-map.md` or equivalent manifest for authoritative artifacts
- require every subagent task to name read set, write set, and verification target
- store intermediate analyses and experiment evidence as first-class files
- keep the coordinator summary short and regenerate it from artifacts when possible
- treat chat as transient control traffic, not the source of truth

## Tools and methodologies worth trying now

- AiScientist
- project manifests or workspace maps
- stage-gated execution
- artifact-based delegation contracts
- repo-local verification checklists
- benchmark loops like PaperBench and MLE-Bench Lite

## Implementability score

0.91

This is highly implementable because it does not require a frontier model breakthrough. It requires discipline in how the runtime uses the filesystem and how orchestration contracts are written.

## Working conclusion

If a long-horizon agent system cannot survive the loss of its chat transcript, it is not really stateful. File-as-Bus is compelling because it moves state into durable, inspectable, operator-friendly artifacts.
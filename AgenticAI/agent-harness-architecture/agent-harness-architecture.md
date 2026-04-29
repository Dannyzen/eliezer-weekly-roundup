# Agent Harness Architecture

Agent harness architecture is becoming the part of the agent stack that teams can actually standardize.

The durable pattern across recent work is simple: the interesting engineering differences are no longer only inside the model. They sit in the non-LLM infrastructure around it — context services, tool mediation, delegation, isolation, orchestration, and safety controls. Once those choices become explicit, agent systems stop looking like prompt tricks and start looking like software architecture.

## Why this topic now

The April 2026 signal is unusually clear:
- **Architectural Design Decisions in AI Agent Harnesses** studies 70 public projects and shows that recurrent design dimensions are now visible enough to classify.
- **Microsoft Agent Framework 1.1.0** turns several of those dimensions into concrete runtime knobs: file history providers, checkpoint allowlists, hosted workflow support, and stronger execution/runtime surfaces.
- **Claude Context** shows another important trend: context handling is externalizing into installable services instead of staying buried inside one agent loop.

Core sources:
- Architectural Design Decisions in AI Agent Harnesses: https://arxiv.org/abs/2604.18071v1
- Microsoft Agent Framework python-1.1.0: https://github.com/microsoft/agent-framework/releases/tag/python-1.1.0
- Microsoft Agent Framework repo: https://github.com/microsoft/agent-framework
- Claude Context: https://github.com/zilliztech/claude-context

## Core thesis

The wrong question is "which agent framework is best?"

The right questions are:
- how does it manage context over long-running work?
- how are tool boundaries declared and governed?
- what isolation or sandbox model exists for risky execution?
- how does it represent subagents and orchestration?
- what evidence does it preserve for replay, audit, and debugging?

If those questions are ignored, teams end up comparing demos instead of systems.

## The five design dimensions that matter

### 1. Subagent architecture
How does the system delegate?

Useful distinctions:
- flat tool-call loops
- hierarchical subagents
- mixed graph-and-agent patterns
- explicit handoff semantics versus ad hoc nested prompts

### 2. Context management
How does state persist and return?

Useful distinctions:
- ephemeral transcript-only context
- file-persistent context
- hybrid context that mixes transcript, files, and structured state
- hierarchical context services with explicit scopes

### 3. Tool systems
How are actions exposed?

Useful distinctions:
- registry-oriented tool catalogs
- MCP-based external tool surfaces
- plugin architectures
- typed versus loosely structured tool interfaces

### 4. Safety mechanisms
Where does control enter the execution path?

Useful distinctions:
- sandbox level
- policy mediation points
- approval gates
- checkpoint restore controls
- auditability of memory, tools, and handoffs

### 5. Orchestration
How is work sequenced?

Useful distinctions:
- prompt-loop orchestration
- workflow graphs
- event-driven orchestration
- resumable execution with checkpoints and replay

## What the recent evidence says

The 70-project harness survey surfaces several regularities that are likely to persist:
- file-persistent, hybrid, and hierarchical context strategies are common in serious systems
- registry-oriented tool systems still dominate, but MCP and plugin extensions are clearly rising
- deeper coordination tends to pair with more explicit context services
- stronger execution environments tend to pair with more structured governance
- intermediate isolation is common, but high-assurance audit is still rare

That last point matters. Many projects have some containment. Very few have governance strong enough to satisfy real operational scrutiny.

## What to build now

### Compare harnesses with a scorecard
Do not choose a framework by vibe.

Score at least these dimensions:
- context persistence model
- tool registration model
- isolation model
- checkpoint and restore policy
- replay and trace quality
- orchestration flexibility

### Treat context as infrastructure
For long-running work, default to:
- file-persistent or hybrid context
- explicit scope boundaries
- structured retrieval or history providers
- clear rules for what becomes durable

### Make tool boundaries governable
A tool system should be legible enough that policy can sit in front of it.

Minimum expectations:
- explicit registration
- typed arguments
- per-tool permissions or policy hooks
- observable tool-call traces

### Bring restore paths under policy
Checkpoint restore is a privileged operation.

Build with:
- type allowlists
- migration rules
- replay visibility
- failure modes that are obvious when state cannot be restored safely

### Separate retrieval services from the core agent loop
External context services and code search surfaces can be a feature, not a smell, when they are inspectable and permissioned.

## What to avoid

Avoid these traps:
- hiding long-term context in one growing transcript buffer
- mixing every tool into one undifferentiated omnipotent catalog
- treating MCP adoption as a substitute for architecture
- assuming sandboxing is binary instead of graded
- restoring opaque checkpoint state without explicit type controls
- shipping multi-agent delegation without replayable evidence

## New April 2026 additions

### Architectural regularities are finally visible
The harness survey is strategically important because it makes agent-system engineering comparable across projects. Five dimensions recur often enough that the field can stop pretending every framework is sui generis.

### Releases are turning those regularities into knobs
Microsoft Agent Framework 1.1.0 is useful because it turns survey dimensions into concrete product surfaces: file history providers, checkpoint allowlists, hosted workflow support, and stronger runtime integrations. The architecture is leaving the whitepaper and entering the runtime.

### Context services are externalizing
Claude Context is good category signal because it treats code retrieval as an installable service rather than a hidden prompt trick. That is the right shape. Context should increasingly look like governed infrastructure.

### Delegation needs contextual calibration, not static role cards
CADMAS-CTX sharpens the subagent point. The same agent can be strong on short edits and weak on long-horizon debugging, so a single global skill label is too blunt. The paper's practical move is to keep per-context capability posteriors and route with an uncertainty penalty. That is a better harness pattern than hard-coded specialist identities or static skill scores.

Practical lesson:
- delegation should depend on context buckets and observed outcomes
- sparse evidence should reduce routing confidence instead of being averaged away
- harnesses need delegation telemetry good enough to learn from comparable situations, not just final task pass rates

Source:
- [CADMAS-CTX](https://arxiv.org/abs/2604.17950)

### Observability-driven harness evolution turns edits into falsifiable contracts
AHE adds the missing improvement loop for this topic. Harnesses should be represented as editable, file-level components; long trajectories should be distilled into layered evidence; and every harness edit should carry a predicted effect that is checked after the next run.

The practical lesson is blunt:
- store harness components as versioned files
- log the component version set with every agent run
- summarize trajectories into evidence that preserves tool calls, failures, patches, and tests
- require harness-edit PRs to declare predicted effects
- replay task suites before adopting scaffold changes

This makes harness engineering falsifiable instead of anecdotal. The exact AHE benchmark numbers will need independent replication, but the control pattern is immediately useful.

Source:
- [Agentic Harness Engineering](https://arxiv.org/abs/2604.25850v1)


## Working conclusion

Agent harness architecture is becoming one of the clearest ways to tell whether a team is building a toy, a developer tool, or a real operating substrate. The winning systems will make context explicit, tool boundaries governable, restore paths safe, orchestration legible, and evidence easy to inspect.
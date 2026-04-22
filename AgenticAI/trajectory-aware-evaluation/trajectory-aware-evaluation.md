# Trajectory-Aware Evaluation

Trajectory-aware evaluation is becoming the dividing line between toy agent demos and systems you can actually improve.

## Core thesis

If you only grade the final output, you are measuring luck, not behavior.

Agent systems act through sequences: planning, tool selection, retries, state changes, recoveries, and handoffs. A benchmark that ignores the sequence cannot reliably tell the difference between:
- a clean execution
- a dangerous execution that happened to end well
- a brittle execution that only works once every few tries
- an execution that silently violated policy before producing a superficially correct answer

## Why this matters

Traditional LLM evals were built for static responses. Agent evals need to answer different questions:
- Did the agent take the right actions?
- Did it stay within policy?
- Did it recover correctly when the environment pushed back?
- Would the behavior repeat across multiple trials?
- Is the trace good enough to audit after a failure?

That means evidence has to come from the run itself, not only the final artifact.

## What a modern agent eval should capture

### 1. Execution traces
Record the actual sequence of actions, tool calls, retries, and branch decisions.

### 2. Environment snapshots
Capture state before, during, and after important actions so graders can verify whether the world changed as intended.

### 3. Audit logs
Preserve policy decisions, approvals, exceptions, and metadata about why actions were allowed or denied.

### 4. Repeated-trial consistency
Use multiple runs per task. A system that passes once in three attempts is not equivalent to a system that passes reliably.

### 5. Separate scoring dimensions
Completion, safety, and robustness should not be collapsed into one opaque metric.

### 6. Parameter-level execution quality
For tool-heavy work, many failures come from wrong arguments, wrong thresholds, and wrong target selection rather than bad intent or bad final prose. Good evals score those execution details directly.

### 7. Modality-aware verification
When outputs are visual, spatial, interactive, or otherwise world-facing, the grader should verify the artifact in the right modality instead of reducing everything to text matching.

## Practical build pattern

A useful minimum stack now looks like this:
1. replayable traces for every run
2. state snapshots at critical checkpoints
3. explicit scoring rubrics for completion, safety, and robustness
4. repeated-trial metrics such as Pass@k and stricter consistency-oriented variants
5. dashboards that let engineers inspect failures by trajectory, not only by top-line score
6. environment-aware checks for parameter correctness and output fidelity

## Tools and methodologies worth exploring now

- OpenTelemetry-style tracing for agent workflows
- environment snapshotting for browser, desktop, or API task state
- rubric-based evaluators linked to traces rather than final outputs only
- perturbation testing to measure recovery and consistency under noise
- benchmark harnesses that preserve evidence artifacts for later replay
- parameter-level execution scoring
- modality-aware verifiers for visual or structured outputs
- adaptive curricula that keep environments near the policy frontier
- runtime-specific safety taxonomies for different execution surfaces

## Representative sources

- Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents: https://arxiv.org/abs/2604.06132
- Microsoft Agent Framework repository, especially its checkpointing and observability features: https://github.com/microsoft/agent-framework
- OpenClaw real-world safety analysis: https://arxiv.org/abs/2604.04759
- GeoAgentBench: https://arxiv.org/abs/2604.13888
- Ecom-RLVE: https://huggingface.co/blog/ecom-rlve
- ATBench-Claw and ATBench-CodeX: https://arxiv.org/abs/2604.14858

## New April 2026 additions

### GeoAgentBench shows why execution metrics need to reach below the final artifact
GeoAgentBench is domain-specific on paper and generally useful in practice. Its main lesson is that tool-augmented agents often fail on the execution substrate: wrong parameters, weak recovery logic, and outputs that need modality-aware verification. Parameter Execution Accuracy is a good pattern because it grades what the agent actually did to the environment, not just whether it wrote a plausible answer afterward.

### Claw-Eval strengthens the case for trace-first grading
Claw-Eval is the clearest current argument that final-output grading is not enough. Its three evidence channels and separate completion, safety, and robustness scores make a good default pattern for future agent benchmarks.

### CodeTracer shows that trace structure matters as much as trace capture
CodeTracer adds an important operational lesson: it is not enough to log everything if the resulting evidence is still too flat to debug. Reconstructing hierarchical state transitions, tagging likely failure onset, and tracing downstream error chains turns observability into something engineers can actually use to recover failed runs.

### EcomRLVE-GYM turns verifiable environments into reusable agent infrastructure
EcomRLVE-GYM adds a useful escalation of the trajectory-aware-eval idea. The environment is not only the place where you score the agent after the fact. It is also the curriculum, the verifier, and the regression harness. Procedural generation, adaptive difficulty, and tuple-level reward computation make the benchmark reusable as training infrastructure.

### ATBench shows safety eval has to adapt to the runtime surface
ATBench-Claw and ATBench-CodeX make an important design correction: the benchmark pipeline can stay shared while the safety taxonomy changes with the runtime. Shells, patches, approvals, sessions, skills, and external actions create different harm surfaces, so the taxonomy has to move with the execution setting.

### Frameworks are starting to absorb evaluation prerequisites
Microsoft Agent Framework is strategically relevant here because checkpointing, time travel, and observability reduce the gap between runtime debugging and benchmark evidence collection. The platform layer is beginning to catch up with what evaluation research actually needs.

### Environment generation turns eval into a service, not a spreadsheet
ClawEnvKit sharpens the next step beyond trace-first evaluation. The benchmark should not only record what happened inside a fixed set of tasks. It should generate new verified tasks when the capability frontier moves. Its parser-generator-validator pipeline and 1,040-environment Auto-ClawEval benchmark make the design pattern clear: a capability description can be compiled into an environment, scored automatically, and recycled into both training and regression testing.

Two lessons matter immediately:
- harness engineering still changes outcomes materially, so eval has to compare scaffolding and not only model families
- operators should be able to describe a desired capability in natural language and get back a verified task world instead of waiting for the next benchmark paper

This is a better product shape for agent evaluation. The environment factory becomes part of the runtime improvement loop.

### Repeated execution is now a first-class reliability test
On the Reliability of Computer Use Agents adds the correction this topic needed. A task is not solved because the agent passed once. The same model can alternate between success and failure across repeated runs due to execution stochasticity, task ambiguity, and behavioral drift. That turns repeated-trial consistency from a nice-to-have into a required metric for browser and desktop agents.

The product lesson is direct:
- rerun the same task multiple times before trusting a pass rate
- record ambiguity and clarification failure as benchmark data, not annotation noise
- optimize for stable strategies across runs instead of one aggressive lucky trajectory

Source:
- [On the Reliability of Computer Use Agents](https://arxiv.org/abs/2604.17849)

## Working conclusion

Trajectory-aware evaluation should become default infrastructure for any team building autonomous or semi-autonomous agents. If the run cannot be replayed, inspected, and scored across safety, robustness, parameter correctness, environment fidelity, and runtime-specific harm dimensions, improvement efforts will stay shallow and trust claims will stay unearned.

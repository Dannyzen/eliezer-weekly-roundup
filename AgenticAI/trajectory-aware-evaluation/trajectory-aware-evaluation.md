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

## Practical build pattern

A useful minimum stack now looks like this:
1. replayable traces for every run
2. state snapshots at critical checkpoints
3. explicit scoring rubrics for completion, safety, and robustness
4. repeated-trial metrics such as Pass@k and stricter consistency-oriented variants
5. dashboards that let engineers inspect failures by trajectory, not only by top-line score

## Tools and methodologies worth exploring now

- OpenTelemetry-style tracing for agent workflows
- environment snapshotting for browser, desktop, or API task state
- rubric-based evaluators linked to traces rather than final outputs only
- perturbation testing to measure recovery and consistency under noise
- benchmark harnesses that preserve evidence artifacts for later replay

## Representative sources

- Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents: https://arxiv.org/abs/2604.06132
- Microsoft Agent Framework repository, especially its checkpointing and observability features: https://github.com/microsoft/agent-framework
- OpenClaw real-world safety analysis: https://arxiv.org/abs/2604.04759

## New April 2026 additions

### Claw-Eval strengthens the case for trace-first grading
Claw-Eval is the clearest current argument that final-output grading is not enough. Its three evidence channels and separate completion, safety, and robustness scores make a good default pattern for future agent benchmarks.

### Frameworks are starting to absorb evaluation prerequisites
Microsoft Agent Framework is strategically relevant here because checkpointing, time travel, and observability reduce the gap between runtime debugging and benchmark evidence collection. The platform layer is beginning to catch up with what evaluation research actually needs.

## Working conclusion

Trajectory-aware evaluation should become default infrastructure for any team building autonomous or semi-autonomous agents. If the run cannot be replayed, inspected, and scored across safety and robustness dimensions, improvement efforts will stay shallow and trust claims will stay unearned.

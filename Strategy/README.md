# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-20

### Distillation pipelines are a governance surface, not a data-cleaning chore
Summary: Trajectory distillation can transfer destructive habits even when explicit keywords are filtered out, so governance has to treat distillation as a behavior pipeline, not just a data-prep step.

Analysis: [sovereignty analysis](2026-04-20/sovereignty.md#distillation-pipelines-are-a-governance-surface-not-a-data-cleaning-chore)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation](https://arxiv.org/abs/2604.15559)
Implementable now:
- run destructive-action canaries before and after trajectory distillation
- keep provenance for teacher models, trajectory corpora, and distillation runs
- sandbox destructive tools even for students trained on supposedly safe traces
- add behavior-level evals that test first-action preferences, not just end-task success
Tools, repos, and methodologies worth exploring:
- [Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation](https://arxiv.org/abs/2604.15559)
- destructive-action canary tasks
- post-distillation behavior regression suites
- sandboxed execution for file and shell actions
- provenance tracking for teacher trajectories and student checkpoints
Implementability score: 0.57

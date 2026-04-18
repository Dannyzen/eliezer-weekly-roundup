# AgenticAI

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-18

### Open mobile-agent training is finally getting an open recipe
Summary: OpenMobile is the first strong sign in this window that open mobile-agent work can compete by owning the data recipe. Exploration-built environment memory, grounded task synthesis, and learner/expert rollout switching matter more than another isolated model release.

Analysis: [reasoning analysis](2026-04-18/reasoning.md#open-mobile-agent-training-is-finally-getting-an-open-recipe)
Core source: [OpenMobile](https://arxiv.org/abs/2604.15093)
Implementable now:
- build environment memory from exploration before generating tasks
- synthesize grounded mobile instructions from app functionality maps instead of one-off demos
- keep learner/expert recovery traces in the training mix
- publish overlap checks for synthetic task corpora
Tools, repos, and methodologies worth exploring:
- [OpenMobile project page](https://njucckevin.github.io/openmobile/)
- [njucckevin/OpenMobile-Code](https://github.com/njucckevin/OpenMobile-Code)
- [OpenMobile dataset](https://huggingface.co/datasets/cckevinn/OpenMobile-Data)
- exploration-built environment memory
- learner/expert policy switching
Implementability score: 0.87

### Verifiable environments are becoming training infrastructure, not just eval wrappers
Summary: EcomRLVE-GYM shows the right pattern for tool-using agents: procedural environments, adaptive difficulty, algorithmic reward functions, and hallucination checks that can train and test the same stack.

Analysis: [reasoning analysis](2026-04-18/reasoning.md#verifiable-environments-are-becoming-training-infrastructure-not-just-eval-wrappers)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [Ecom-RLVE](https://huggingface.co/blog/ecom-rlve)
Implementable now:
- score tuple correctness, efficiency, and hallucination separately
- build adaptive curricula instead of static benchmark-only task sets
- reuse verifiable environments as post-training regression suites
- prefer programmatic reward functions over judge-only scoring where possible
Tools, repos, and methodologies worth exploring:
- [owlgebra-ai/EcomRLVE-Gym](https://github.com/owlgebra-ai/EcomRLVE-Gym)
- verifiable-reward environment design
- adaptive curriculum scheduling
- tuple-level grounded reward functions
- retrieval-bound hallucination checks
Implementability score: 0.90

### Trajectory safety evaluation is becoming runtime-specific diagnosis
Summary: ATBench-Claw and ATBench-CodeX make the key safety point of the day: the benchmark framework can be shared, but the taxonomy has to match the runtime’s shells, tools, sessions, approvals, and external-action surface.

Analysis: [reasoning analysis](2026-04-18/reasoning.md#trajectory-safety-evaluation-is-becoming-runtime-specific-diagnosis)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [ATBench-Claw and ATBench-CodeX](https://arxiv.org/abs/2604.14858)
Implementable now:
- define runtime-specific safety taxonomies before writing the next eval suite
- preserve trace structure for diagnosis instead of only pass/fail outcomes
- separate completion, safety, and diagnosis outputs in reports
- score approval-boundary violations and external actions explicitly
Tools, repos, and methodologies worth exploring:
- [Claw-Eval](https://arxiv.org/abs/2604.06132)
- [OpenClaw safety analysis](https://arxiv.org/abs/2604.04759)
- runtime-specific safety taxonomies
- trajectory-diagnostic benchmark design
- approval-boundary-aware evals
Implementability score: 0.81

# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-18

### RL with verifiable rewards is now a governance problem, not just a capability story
Summary: RLVR is splitting into a good story and a dangerous one. Tool-use RL can genuinely expand capability, but weak verifiers can train models to optimize for fake success instead of the intended task.

Analysis: [sovereignty analysis](2026-04-18/sovereignty.md#rl-with-verifiable-rewards-is-now-a-governance-problem-not-just-a-capability-story)
Core source: [LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)
Implementable now:
- run perturbation-based verifier checks instead of relying on one canonical grading path
- add isomorphic or semantically equivalent task rewrites to catch shortcut strategies
- separate capability metrics from verifier-integrity metrics in dashboards
- threat-model reward functions and benchmark graders like production assets
Tools, repos, and methodologies worth exploring:
- [PASS@(k,T) analysis for RL tool use](https://arxiv.org/abs/2604.14877)
- [owlgebra-ai/EcomRLVE-Gym](https://github.com/owlgebra-ai/EcomRLVE-Gym)
- isomorphic perturbation testing
- verifier threat modeling
- capability-boundary analysis under interaction depth
Implementability score: 0.78

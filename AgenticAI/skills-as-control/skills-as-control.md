# Skills as Control

Last updated: 2026-04-26

Core sources:
- From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation: https://arxiv.org/abs/2604.21910v1
- Agentic AI-assisted coding offers a unique opportunity to instill epistemic grounding during software development: https://arxiv.org/abs/2604.21744v1
- Thinking with Reasoning Skills: Fewer Tokens, More Accuracy: https://arxiv.org/abs/2604.21764v1
- AEL: Agent Evolving Learning for Open-Ended Environments: https://arxiv.org/abs/2604.21725v1
- OpenAI Codex plugins and skills: https://openai.com/academy/codex-plugins-and-skills
- ComposioHQ/awesome-codex-skills: https://github.com/ComposioHQ/awesome-codex-skills

## Thesis

Skills are not just reusable prompt snippets. In serious agent systems, skills are becoming a control layer: reviewed, scoped, versioned procedural knowledge that constrains model behavior, translates domain language into structured intents, and lets deterministic code perform the final execution.

The pattern is strongest when the LLM is allowed to interpret ambiguous human intent but is not allowed to improvise domain rules, validity constraints, workflow topology, or execution semantics.

## April 26 distribution update: skills are becoming packages

The newest practical signal is that skills are becoming installable packages. OpenAI’s Codex docs define a skill as a playbook Codex can follow for a team-specific process, distinct from a plugin that connects Codex to an external tool or source of information. That boundary is important: plugins grant access; skills constrain procedure.

`ComposioHQ/awesome-codex-skills` turns the pattern into a distribution format. It uses `$CODEX_HOME/skills`, per-skill folders, required `SKILL.md` metadata, optional `scripts/`, `references/`, and `assets/`, and an installer that fetches skills from GitHub. The README also describes progressive disclosure: load metadata to decide whether a skill applies, then load the body only after the skill fires.

That turns the skill from a prompt trick into a software artifact. It can be pinned, reviewed, installed, tested, shared, deprecated, and audited.

## Architecture pattern

1. User goal arrives in natural language.
2. The agent retrieves a small set of relevant skills or grounding documents.
3. The model maps the goal into a typed intent or plan while citing the skill sections it used.
4. Deterministic generators, validators, or tools convert the typed intent into artifacts: DAGs, code, config, test cases, or operational steps.
5. Runtime traces preserve which skills were applied, which constraints were checked, and where execution diverged.
6. Repeated successful trajectories are proposed as new or updated skills only after review.

## What belongs in a skill

Good skills should separate:
- hard constraints: invariants the agent must not violate;
- convention parameters: defaults that are usually right but can be overridden deliberately;
- vocabulary mappings: domain words to schemas, APIs, or workflow objects;
- decision rules: when to choose one path over another;
- examples: short, high-signal cases that clarify boundary conditions;
- tests: checks that prove the skill constrained behavior correctly;
- deterministic helpers: scripts, templates, schemas, or small tools that prevent the model from improvising brittle steps;
- long references: loaded only when needed, not pasted into every turn.

Bad skills are long transcripts, motivational prose, stale checklists, unpinned third-party installers, or untested instructions that silently override newer project facts.

## Why this matters for the agentic stack

The science-workflow paper shows the implementation payoff: Skills improved full-match intent accuracy from 44% to 83%, reduced data transfer by 92% through deferred workflow generation, and kept LLM overhead below 15 seconds with sub-mill cent query cost in the reported Kubernetes setup.

The GROUNDING.md paper shows the governance payoff: field-scoped documents can encode non-negotiable scientific or engineering constraints so non-experts can still generate code that respects domain validity.

The reasoning-skills paper shows the cost payoff: reusable distilled reasoning routines can cut redundant reasoning tokens and improve accuracy.

AEL adds the discipline: memory and reflection help, but piling on more self-improvement mechanisms can degrade outcomes. Skills need to be compact, useful, and tested.

The Codex/Composio packaging pattern adds the operational payoff: skills can be distributed and updated like internal libraries, with metadata-triggered loading instead of always-on context bloat.

## Implementation checklist

- Add `GROUNDING.md` or `SKILLS.md` at the repo, domain, and method levels where agents repeatedly work.
- Package recurring workflows as folders with `SKILL.md`, optional `scripts/`, `references/`, `templates/`, and tests.
- Label sections as hard constraints, conventions, examples, and tests.
- Require agents to cite applied skill sections in plans or generated artifacts.
- Convert plans into typed intents before deterministic execution.
- Pin third-party skill installers or skill repos to reviewed commits.
- Add regression tests that intentionally tempt the agent to violate hard constraints.
- Version skills like source code and review changes before they become default behavior.
- Deprecate or remove skills that are stale, overbroad, or no longer tested.

## Pitfalls

- Treating every remembered fact as a skill.
- Letting skills become huge context dumps.
- Allowing stale skills to outrank current repository state.
- Encoding preferences as hard constraints without owner review.
- Skipping tests, which turns a skill into another unverified prompt.
- Hiding domain assumptions inside examples instead of stating them as constraints.
- Installing community skills without supply-chain review.
- Confusing plugins that grant access with skills that guide process.

## Implementability score

0.94

The pattern is implementable immediately with markdown files, metadata, deterministic helper scripts, retrieval, typed schemas, and regression tests. The remaining hard work is lifecycle management: review, versioning, applicability scoring, deprecation, and supply-chain safety for shared skills.

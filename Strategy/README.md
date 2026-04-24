# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-24

### Sovereignty is routing plus privacy filtering plus local grounding
Summary: The sovereign-agent story is maturing beyond “run the model locally.” This week’s strongest pattern combines local privacy filters, capability-shaped local benchmarks, edge multimodal demos, cloud escalation, and region-specific grounding data.

Analysis: [sovereignty analysis](2026-04-24/sovereignty.md#sovereignty-is-routing-plus-privacy-filtering-plus-local-grounding)
Durable topic: [Local-First Agents](local-first-agents/local-first-agents.md)
Core source: [Introducing OpenAI Privacy Filter](https://openai.com/index/introducing-openai-privacy-filter)
Supporting sources:
- [Benchmarking System Dynamics AI Assistants](https://arxiv.org/abs/2604.18566)
- [Gemma 4 VLA Demo on Jetson Orin Nano Super](https://huggingface.co/blog/nvidia/gemma4)
- [How to Ground a Korean AI Agent in Real Demographics with Synthetic Personas](https://huggingface.co/blog/nvidia/build-korean-agents-with-nemotron-personas)
- [Atropos](https://arxiv.org/abs/2604.15075)
Implementable now:
- redact or mask PII locally before retrieval ingestion, logging, training-data prep, or cloud escalation
- route structured extraction and narrow local multimodal tasks to local models first
- benchmark task shapes, not ideology: extraction, discussion, correction, vision-action, and escalation are different workloads
- treat local grounding datasets as strategic assets next to model weights and routing policy
Tools, repos, and methodologies worth exploring:
- OpenAI Privacy Filter
- Gemma 4 on Jetson or other constrained edge devices
- local-first benchmark suites by task family
- hybrid routing policies with explicit escalation triggers
Implementability score: 0.90

### Runtime containment is moving from policy document to product surface
Summary: High-autonomy agents are forcing containment into the tool itself. Shannon v1.1.0’s read-only repo mounts, writable overlays, structured exploit queues, and provider abstraction are a practical example of governance becoming runtime design.

Analysis: [sovereignty analysis](2026-04-24/sovereignty.md#runtime-containment-is-moving-from-policy-document-to-product-surface)
Durable topic: [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md)
Core source: [Shannon v1.1.0](https://github.com/KeygraphHQ/shannon/releases/tag/v1.1.0)
Supporting source: [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)
Implementable now:
- mount target repositories read-only and give agents separate writable overlays
- run high-risk agent work inside disposable workers or self-hosted runners
- preserve exploit queues, traces, and reports as audit artifacts
- surface Docker or worker errors to operators instead of hiding containment failures
Tools, repos, and methodologies worth exploring:
- Shannon Lite
- Incus/LXC or microVM-backed workspaces
- read-only source mounts plus writable overlays
- structured output queues for high-risk agent actions
Implementability score: 0.92

### Distillation and verifier training need governance before deployment
Summary: The week’s RL and distillation work makes a hard governance point: reward hacking and inherited unsafe behavior are training-pipeline risks, not just runtime guardrail problems.

Analysis: [sovereignty analysis](2026-04-24/sovereignty.md#distillation-and-verifier-training-need-governance-before-deployment)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)
Supporting source: [Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation](https://arxiv.org/abs/2604.15559)
Implementable now:
- treat verifiers as attack surfaces and test for reward hacking before scaling RLVR loops
- run destructive-action canaries on distilled agents even when training traces look clean
- preserve trajectory provenance for demonstration datasets and student checkpoints
- sandbox agents during post-training evaluation, not only after deployment
Tools, repos, and methodologies worth exploring:
- verifier adversarial test suites
- sandboxed RL rollouts
- behavior-transfer probes for distilled agents
- training-data lineage and signed trajectory stores
Implementability score: 0.57

### Specialized agent infrastructure is useful bottleneck evidence and a lock-in warning
Summary: Google’s TPU 8t/8i split is vendor positioning, but it exposes real agent-serving bottlenecks: tail latency, KV-cache residency, MoE routing, memory bandwidth, collectives, and synchronization across multi-agent workflows.

Analysis: [sovereignty analysis](2026-04-24/sovereignty.md#specialized-agent-infrastructure-is-useful-bottleneck-evidence-and-a-lock-in-warning)
Core source: [Our eighth generation TPUs: two chips for the agentic era](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
Supporting source: [TPU 8t and TPU 8i technical deep dive](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)
Implementable now:
- measure agent-loop latency by model call, tool call, routing decision, and synchronization point
- separate training, post-training, and serving requirements in infrastructure scorecards
- benchmark vLLM or SGLang under multi-agent workloads, not only single-prompt throughput
- keep portability and fallback paths explicit before tuning too tightly to a vendor’s stack
Tools, repos, and methodologies worth exploring:
- vLLM and SGLang multi-agent serving tests
- tail-latency budgets for agent orchestration
- KV-cache and MoE routing telemetry
- local/commodity/cloud routing policies
Implementability score: 0.32

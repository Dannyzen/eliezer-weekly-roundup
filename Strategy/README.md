# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-24

### Google is splitting cloud AI hardware around agentic serving
Summary: TPU 8t and TPU 8i show that agent infrastructure is no longer one generic accelerator story. Training, post-training, and low-latency agent serving are separating into different hardware and orchestration paths.

Analysis: [sovereignty analysis](2026-04-24/sovereignty.md#google-is-splitting-cloud-ai-hardware-around-agentic-serving)
Core source: [Our eighth generation TPUs: two chips for the agentic era](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
Supporting source: [TPU 8t and TPU 8i technical deep dive](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)
Implementable now:
- measure agent-loop latency by model call, tool call, routing decision, and synchronization point
- separate training, post-training, and serving requirements in infrastructure plans
- benchmark vLLM or SGLang under multi-agent workloads instead of only single-prompt throughput
- track KV-cache residency, context length, and MoE routing overhead as cost drivers
- make cloud-specialization versus portability an explicit procurement decision
Tools, repos, and methodologies worth exploring:
- Google TPU 8t/8i announcement and technical deep dive
- vLLM and SGLang multi-agent serving tests
- tail-latency budgets for agent orchestration
- infrastructure scorecards separating training, post-training, and serving
- local/commodity/cloud routing policies for agent workloads
Implementability score: 0.32

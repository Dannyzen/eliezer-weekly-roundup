# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-04-29

### MCP semantic gateways are becoming the enterprise agent control plane
Summary: The Semantic Gateway paper reframes enterprise APIs as governed semantic tool surfaces for autonomous agents. The key pattern is MCP discovery behind identity, semantic firewalls, deterministic tool-level RBAC, cryptographic human approval, enabled-tool graph fuzzing, tracing, and audit. Jarvis Registry is a practical open-source signal in the same direction.

Analysis: [sovereignty analysis](2026-04-29/sovereignty.md#mcp-semantic-gateways-are-becoming-the-enterprise-agent-control-plane)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [From CRUD to Autonomous Agents](https://arxiv.org/abs/2604.25555v1)
Supporting source:
- [Jarvis Registry](https://github.com/ascending-llc/jarvis-registry)
Implementable now:
- put a gateway in front of internal MCP servers and privileged tool APIs
- assign identities and scopes to each agent workflow
- enforce tool-level RBAC before execution
- record policy decisions and approval artifacts in the trace
- fuzz multi-turn trajectories against unauthorized-state goals
Tools, repos, and methodologies worth exploring:
- Jarvis Registry or equivalent MCP/A2A gateway patterns
- Keycloak, Cognito, or Entra ID
- Open Policy Agent or Cedar
- OpenTelemetry and Prometheus
- enabled-tool graph fuzzing
Implementability score: 0.76

### Managed cloud agents and open omni models create a routing-governance split
Summary: OpenAI on AWS and NVIDIA Nemotron 3 Nano Omni point to a strategic fork: enterprises can buy managed OpenAI models/Codex/agents inside AWS controls, while open multimodal checkpoints make private document/audio/video/screen reasoning more feasible. The router now has to govern modality, sensitivity, residency, cost, and tool authority.

Analysis: [sovereignty analysis](2026-04-29/sovereignty.md#managed-cloud-agents-and-open-omni-models-create-a-routing-governance-split)
Durable topic: [Model Router Governance](model-router-governance/model-router-governance.md)
Core sources:
- [OpenAI models, Codex, and Managed Agents come to AWS](https://openai.com/index/openai-on-aws)
- [NVIDIA Nemotron 3 Nano Omni](https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence)
Implementable now:
- classify tasks by sensitivity and modality before model selection
- route sensitive document/audio/video preprocessing to private or local paths where feasible
- use managed cloud agents where procurement, identity, and compliance fit
- log effective provider, model, modality path, and routing reason
- test fallback behavior against privacy and residency policy
Tools, repos, and methodologies worth exploring:
- Amazon Bedrock and Codex on AWS
- Hugging Face checkpoints for Nemotron 3 Nano Omni
- LiteLLM-style policy-aware routing
- vLLM, TensorRT-LLM, and NVIDIA inference tooling
- routing traces and fallback-policy tests
Implementability score: 0.63

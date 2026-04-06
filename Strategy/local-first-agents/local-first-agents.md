# Local-First Agents

Local-first agents matter because they change the default trust boundary. Instead of shipping every user interaction, screenshot, document, and tool call to a hosted endpoint, more of the workflow can remain on the device or within a tightly controlled edge environment.

## Why this topic now

The April 2026 Gemma 4 release plus LiteRT-LM support is the clearest recent signal that local-first agent design is becoming practical rather than aspirational. The stack now includes:
- open Apache 2.0 multimodal models
- local runtimes with constrained decoding and tool calling
- mobile, desktop, browser, and Raspberry Pi deployment paths
- enough context length and multimodal ability to support real agent tasks

Core sources:
- Google Developers Blog: https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/
- Hugging Face Gemma 4 launch post: https://huggingface.co/blog/gemma4
- LiteRT-LM release v0.10.1: https://github.com/google-ai-edge/LiteRT-LM/releases/tag/v0.10.1

## What local-first actually buys you

### 1. Tighter privacy by default
Sensitive context can stay on-device instead of being sent upstream by default. That matters for enterprise documents, screenshots, email, meeting notes, and personally identifying information.

### 2. Lower and more predictable latency
For short-turn interactions and local tool calls, on-device execution avoids network round trips and can feel dramatically more responsive.

### 3. Better resilience
A local-first workflow can keep functioning with poor connectivity or during provider outages. That changes the reliability story for mobile, field, and embedded use cases.

### 4. Clearer routing choices
Once local execution is viable, cloud usage becomes a deliberate escalation path instead of an assumption.

## What it does not solve

Local-first does not magically solve:
- unsafe tool invocation
- weak policy enforcement
- memory poisoning or retrieval mistakes
- poor auditability
- brittle multi-step planning

A sovereign stack still needs runtime controls, approval gates, constrained outputs, and narrow scopes.

## Practical stack to try now

### Models
- Gemma 4 E2B and E4B for smaller multimodal local workloads
- Larger Gemma 4 variants when local hardware budget allows

### Runtimes and tools
- LiteRT-LM for local inference, constrained decoding, speculative decoding, and tool calling
- Google AI Edge Gallery for rapid experimentation with on-device agent skills
- llama.cpp, MLX, or transformers where they fit better than LiteRT-LM on current hardware

### Methodologies
- Route private and latency-sensitive subtasks to local models first
- Use cloud models only for overflow cases that need more capability
- Log which tasks remain local versus escalated so routing policy can improve over time
- Keep memory and tool execution under explicit policy even when the model runs locally

## Selection rubric

Use local-first first when the workload has one or more of these properties:
- sensitive user data or regulated content
- intermittent connectivity
- low-latency interaction requirements
- narrow task surface that fits within a smaller capable model
- repeated workflows where stable local deployment is worth setup effort

Use cloud-first when the workload needs:
- maximum frontier reasoning quality every turn
- large-scale shared memory or coordination across users
- elastic compute for rare heavy spikes
- provider-managed evaluation, observability, or compliance features you do not want to build yet

## Current read

The important shift is not that local models beat every hosted model. They do not. The shift is that local-first is now viable enough to become the default for a meaningful slice of agent workloads. That forces better architecture decisions: explicit routing, explicit scopes, and explicit reasons for what leaves the device.

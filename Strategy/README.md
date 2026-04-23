# Strategy

This index tracks the most recent week with structured content. Each finding includes a short summary, a link into the detailed analysis, a core source, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Week: 2026-04-23

### Privacy filters are becoming the practical boundary before cloud escalation
Summary: A small open-weight privacy model that runs locally is more strategically useful than another abstract privacy promise. Redact first, then decide what is allowed to leave the boundary.

Analysis: [sovereignty analysis](2026-04-23/sovereignty.md#privacy-filters-are-becoming-the-practical-boundary-before-cloud-escalation)
Core source: [Introducing OpenAI Privacy Filter](https://openai.com/index/introducing-openai-privacy-filter)
Implementable now:
- run local privacy filtering before sending tickets, notes, logs, or transcripts to hosted models
- scrub secrets and identifiers before indexing internal corpora
- fine-tune the filter to local policy rather than trusting default masking rules blindly
- reserve human review for high-sensitivity or low-confidence cases
Tools, repos, and methodologies worth exploring:
- [openai/privacy-filter](https://github.com/openai/privacy-filter)
- [openai/privacy-filter on Hugging Face](https://huggingface.co/openai/privacy-filter)
- local redaction gates before cloud escalation
- in-domain privacy evaluation suites
- [Local-First Agents](local-first-agents/local-first-agents.md)
Implementability score: 0.95

### Edge multimodal agents are now credible on commodity boards
Summary: A Jetson-class local stack with Gemma 4, `llama.cpp`, Parakeet, Kokoro, and one explicit vision tool shows that multimodal agents can stay on-device when the action surface is narrow.

Analysis: [sovereignty analysis](2026-04-23/sovereignty.md#edge-multimodal-agents-are-now-credible-on-commodity-boards)
Durable topic: [Local-First Agents](local-first-agents/local-first-agents.md)
Core source: [Gemma 4 VLA Demo on Jetson Orin Nano Super](https://huggingface.co/blog/nvidia/gemma4)
Supporting source: [asierarranz/Google_Gemma](https://github.com/asierarranz/Google_Gemma)
Implementable now:
- stand up a local multimodal assistant on Jetson-class hardware with an OpenAI-compatible local endpoint
- keep the tool surface to one or two explicit actions instead of a broad workstation abstraction
- benchmark quant choices and memory cleanup before scaling hardware budgets
- use local-first multimodal assistants for narrow workflows before attempting general autonomy
Tools, repos, and methodologies worth exploring:
- [Gemma 4 VLA Demo on Jetson Orin Nano Super](https://huggingface.co/blog/nvidia/gemma4)
- [asierarranz/Google_Gemma](https://github.com/asierarranz/Google_Gemma)
- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
- [unsloth/gemma-4-E2B-it-GGUF](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF)
- Parakeet STT and Kokoro TTS
Implementability score: 0.88

# Track 2 — LLM Inference Optimization
Goal: a **defended serving configuration**. The full track serves with vLLM on a real GPU; the built lab covers the levers you can measure **free**.

## ▶️ Available now
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/02_inference/lab04_inference_optimization.ipynb)

**`lab04_inference_optimization.ipynb`** — exact + semantic **caching**, **model routing** (8B ↔ 70B),
and **context trimming**, each costed on p50/p95 latency and $/query against the banking eval set.
*Simplified vs. the full track:* no GPU serving — batching, KV/prefix cache, quantization and
speculative decoding need vLLM on a dedicated box (rows ⏳ below). The discipline is identical:
measure p95 and $/query, change one lever, re-measure.

## Full track roadmap
*The complete track we're building toward. The lab above is the runnable, free-tier core; rows marked ⏳ are planned, not yet in the repo.*

| Lab | Studies | Free stack | Status |
|---|---|---|---|
| I-free | caching, routing, context trim | Groq + in-memory cache | ✅ built (`lab04`) |
| I0 | benchmark harness | Locust, Prometheus+Grafana | ⏳ planned |
| I2 | batching | vLLM static vs continuous | ⏳ planned |
| I3 | KV & prefix caching | vLLM `--enable-prefix-caching` | ⏳ planned |
| I4 | quantization | AutoAWQ, GPTQ, bitsandbytes | ⏳ planned |
| I5 | speculative decoding | vLLM + Llama 3.2 1B draft | ⏳ planned |
| I7 | serving shoot-out | vLLM / TGI / SGLang / Ollama | ⏳ planned |

**Discovery:** most of the free wins are caching and routing; the GPU-serving track is where the last order of magnitude lives.

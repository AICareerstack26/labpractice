# GenAI Deep-Dive Practicum — Meridian Bank

Hands-on GenAI engineering on one running scenario — **Meridian Bank** — where every lab is
**free to run on Google Colab** and emits into one shared observability + evaluation spine.

> **The rule this repo enforces:** build the measuring instrument before the thing. Every lab
> imports `common.harness.evaluate()` and tags its run with a config hash, so comparisons happen
> automatically instead of in a spreadsheet.

## ▶️ Available now — 8 runnable labs
Open any of these in Colab (add `GROQ_API_KEY` + optional Langfuse keys in Colab Secrets):

| # | Lab | What you build | Open |
|---|---|---|---|
| 0 | Observability & Eval Harness | tracing + a golden eval set, **first** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/00_foundation/lab00_observability_eval.ipynb) |
| 1 | Ingestion & Parsing | a clean corpus from messy bank docs | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/01_rag/lab01_ingestion_parsing.ipynb) |
| 2 | Chunking, Measured | every chunker scored by doctype | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/01_rag/lab02_chunking.ipynb) |
| 3 | Retrieval & Reranking | dense/BM25/hybrid + rerank + version filter | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/01_rag/lab03_retrieval_reranking.ipynb) |
| 4 | Inference Optimization | caching, routing, trimming — costed | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/02_inference/lab04_inference_optimization.ipynb) |
| 5 | Fine-tuning the Retriever | embedding fine-tune, proven on the harness | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/03_finetuning/lab05_finetuning.ipynb) |
| 6 | The Agentic Layer | a bounded agent loop with tools | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/04_agentic/lab06_agentic.ipynb) |
| 7 | MCP Integration & Scopes | FastMCP tools + per-role least privilege | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/05_mcp/lab07_mcp.ipynb) |

Work through them in order and you have a defensible, end-to-end GenAI system in your portfolio.

## Setup (Colab — the quick path)
1. Click any **Open in Colab** badge above.
2. In Colab: **🔑 (sidebar) → Secrets** → add `GROQ_API_KEY` (free: console.groq.com) and, optionally,
   `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` (free: cloud.langfuse.com). Toggle *Notebook access* on.
3. Run the first cell — it installs deps and clones this repo for the shared `common/` package.
   *(If you hit a `PIL._typing._Ink` error: run the cell, then Runtime → Restart session, then re-run.)*

Labs run **without** the Langfuse keys — tracing is simply skipped.

## Cost
£0. Local `bge` embeddings, free-tier LLM APIs (Groq), OSS observability (Langfuse), and a free Colab T4.

## Roadmap (being built)
Each track has a fuller curriculum planned — see the per-folder `README.md` for the roadmap
(vector-store tuning, generation/grounding, RAG architectures, quantization & vLLM serving,
LLM QLoRA/DPO, agent memory & multi-agent, MCP contract testing) and the `99_capstone/` finale.
Labs above are the built, runnable subset; the rest are marked ⏳ in each track.

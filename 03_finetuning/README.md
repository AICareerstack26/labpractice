# Track 3 — Fine-tuning
**Rule: you may not fine-tune until prompting is exhausted and measured.**

## ▶️ Available now
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/03_finetuning/lab05_finetuning.ipynb)

**`lab05_finetuning.ipynb`** — the highest-ROI, genuinely-free fine-tune for RAG: **fine-tune the
embedding model** on your own corpus and prove the retrieval lift on the harness. Teaches why
fine-tuning changes *behaviour*, not *knowledge*.
*Simplified vs. the full track:* LLM QLoRA/DPO (Unsloth/TRL) and adapter serving are ⏳ below —
reach for them only when you need a specific format/tone the base model won't hold.

## Full track roadmap
*The complete track we're building toward. The lab above is the runnable, free-tier core; rows marked ⏳ are planned, not yet in the repo.*

| Lab | Studies | Free stack | Status |
|---|---|---|---|
| F-free | embedding fine-tune, proven on harness | sentence-transformers | ✅ built (`lab05`) |
| F0 | prompting baseline | few-shot, structured | ⏳ planned |
| F2 | SFT with PEFT | Unsloth on free Colab | ⏳ planned |
| F4 | preference tuning | TRL DPO / ORPO | ⏳ planned |
| F5 | structured extraction | Outlines, Qwen2.5 | ⏳ planned |
| F7 | serving adapters | vLLM multi-LoRA | ⏳ planned |

**Central discovery:** fine-tuning reliably changes behaviour/format/tone; it is an expensive, unreliable way to add knowledge — that is RAG's job.

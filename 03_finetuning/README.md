# Track 3 — Fine-tuning  (Curriculum §5)
**Rule: you may not fine-tune until prompting is exhausted and measured (F0).**

| Lab | Studies | Free stack | Key metric |
|---|---|---|---|
| F0 | Prompting baseline | few-shot, structured prompts | the number fine-tuning must beat |
| F1 | Dataset construction | distilabel, MinHash dedup | leakage-free split; size-vs-gain curve |
| F2 | SFT with PEFT | **Unsloth** on free Colab/Kaggle | LoRA rank/alpha/target-module sweep |
| F3 | Full FT vs PEFT | TRL | quality delta vs **catastrophic forgetting** |
| F4 | Preference tuning | TRL DPO / ORPO | refusal correctness, tone adherence |
| F5 | Structured extraction | Outlines / guidance, Qwen2.5 | **schema compliance %**, field F1 |
| F6 | Evaluation | task + general regression | contamination check |
| F7 | Serving adapters | vLLM multi-LoRA | merged vs runtime, switch cost |

**Central discovery:** fine-tuning reliably changes *behaviour/format/tone*; it is an
expensive, unreliable way to add *knowledge*. Prove it in F5 against a RAG baseline.

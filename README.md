# GenAI Deep-Dive Practicum — Working Repo

Companion code for the **GenAI Deep-Dive Practicum** curriculum (Meridian Bank scenario).
Every lab is runnable, free to run, and emits into one shared observability spine.

## The rule this repo enforces
> **Build the measuring instrument before the thing.**
> Every lab imports `common.harness.evaluate()` and tags its run with a config hash,
> so comparisons happen automatically instead of in a spreadsheet.

## Layout
| Folder | Curriculum section | Contents |
|---|---|---|
| `common/` | — | Shared corpus, golden set, scorers, observability, harness |
| `00_foundation/` | §2 Lab 0 | Observability + evaluation spine — **start here** |
| `01_rag/` | §4 Track 1 | Labs R1–R8: parsing → chunking → embeddings → index → retrieval → generation → architectures → production |
| `02_inference/` | §5 Track 2 | Labs I0–I8: benchmarking, batching, KV cache, quantization, routing, serving |
| `03_finetuning/` | §5 Track 3 | Labs F0–F7: dataset, LoRA/QLoRA, DPO, extraction, serving adapters |
| `04_agentic/` | §5 Track 4 | Labs A0–A7: loop, tools, memory, planning, multi-agent, guardrails |
| `05_mcp/` | §5 Track 5 | Labs M0–M5: server, primitives, scopes, contract tests |
| `99_capstone/` | §8 | Integrated Meridian assistant |
| `data/` | — | Generated corpus + artefacts |
| `results/` | — | Leaderboards written by each lab |

## Setup (once)

### Windows one-time fix (avoids a path-length install error)
Run in an **Administrator PowerShell**, then reboot:
```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

### Local (laptop / CPU) — RAG, Agentic, MCP tracks
```bash
cd genai_practical
python -m venv .venv && .venv\Scripts\activate            # Windows
pip install torch --index-url https://download.pytorch.org/whl/cpu   # CPU wheel FIRST
pip install -r requirements-local.txt
docker compose up -d                                      # Langfuse, Qdrant, Redis, Phoenix
```
> **Why torch-cpu first:** the default `torch` is the multi-GB CUDA build whose deeply-nested
> license files break the Windows 260-char path limit. The CPU wheel is smaller, sidesteps it,
> and is all the RAG / Agentic / MCP tracks need.

### Colab / Kaggle (GPU) — Fine-tuning & Inference tracks
GPU + CUDA torch already present — **do not reinstall torch**:
```python
!pip install -r requirements-colab.txt
```
Then open http://localhost:3000 (Langfuse), create a project, copy the keys into `.env`:
```
LANGFUSE_HOST=http://localhost:3000
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
GROQ_API_KEY=gsk_...        # free tier: console.groq.com
```

## Order to run
1. `00_foundation/lab00_observability_eval.ipynb` — **mandatory first**
2. `01_rag/lab01…lab08` in order
3. Then Tracks 2–5 in any order (each has its own Lab 0-equivalent harness)

## Cost
£0. Local embeddings (CPU), local vector stores, free-tier LLM APIs, OSS observability. The Fine-tuning and Inference tracks run free on Colab/Kaggle GPUs.

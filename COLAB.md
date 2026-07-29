# Running on Google Colab (recommended)

You do **not** need Docker or a local install. Free GPU + free observability dashboard.

## One-time setup (5 min)
1. **Get free keys**
   - Langfuse (dashboard): https://cloud.langfuse.com  → create project → copy Public + Secret key
   - Groq (fast free LLM): https://console.groq.com  → API Keys
2. **Put the repo where Colab can see it** — pick one:
   - **Google Drive:** upload/unzip the `genai_practical` folder to `MyDrive/genai_practical` (the bootstrap auto-mounts Drive)
   - **GitHub:** push the repo, then set `REPO_URL` in the bootstrap cell and uncomment the clone line
3. **Add keys to Colab Secrets** (🔑 icon, left sidebar): `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `GROQ_API_KEY` — toggle *Notebook access* ON for each.

## Run
Open a lab in Colab → **Runtime → Change runtime type → T4 GPU** → run the **Colab setup** cell first, then top-to-bottom.

## What runs where
| Track | Colab free tier |
|---|---|
| RAG (R1–R8) | ✅ T4 or even CPU |
| Inference (I0–I8) | ✅ T4 — the GPU is the point |
| Fine-tuning (F0–F7) | ✅ T4 via Unsloth (or Kaggle 30h/wk for longer runs) |
| Agentic (A0–A7) | ✅ CPU fine |
| MCP (M0–M5) | ✅ CPU fine |

## No signups? Still works.
Skip the Secrets step. `common/obs.py` detects missing keys and runs **offline** — every lab
still executes and prints its leaderboard; you just lose the Langfuse UI.

## Vector stores on Colab
- **FAISS** (default in R1–R4): in-memory, nothing to install beyond `faiss-cpu`. ✅
- **Qdrant** (R4 filtering, A3 memory): use the free 1GB cloud cluster at cloud.qdrant.io, or run it in-process.
- **Redis** (semantic cache, agent memory): free 30MB at Redis Cloud, or swap for an in-memory dict for learning.

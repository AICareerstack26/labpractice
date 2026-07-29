"""Central configuration. Every lab imports from here so runs stay comparable."""
import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
import os as _os
_os.environ.setdefault("LANGFUSE_HOST", "https://cloud.langfuse.com")

DATA    = ROOT / "data";    DATA.mkdir(exist_ok=True)
RESULTS = ROOT / "results"; RESULTS.mkdir(exist_ok=True)

# "Today" for the copilot. Policy v3 (effective 2026-04-01) is in force.
AS_OF = os.getenv("AS_OF_DATE", "2026-07-01")

# --- Free model catalogue (curriculum §1) -------------------------------
EMBED_MODELS = {
    "tiny":  "sentence-transformers/all-MiniLM-L6-v2",   # 384  - floor baseline
    "small": "BAAI/bge-small-en-v1.5",                   # 384  - fast
    "base":  "BAAI/bge-base-en-v1.5",                    # 768  - usual sweet spot
    "large": "BAAI/bge-large-en-v1.5",                   # 1024 - quality end
    "e5":    "intfloat/e5-base-v2",                      # 768  - different recipe
    "nomic": "nomic-ai/nomic-embed-text-v1.5",           # 768  - Matryoshka (R3 truncation lab)
}
RERANKERS = {
    "bge":    "BAAI/bge-reranker-v2-m3",
    "mxbai":  "mixedbread-ai/mxbai-rerank-base-v1",
}
# Free-tier generation. Groq is fast and free; swap for Gemini/Ollama as you like.
GEN_MODEL   = os.getenv("GEN_MODEL",   "llama-3.3-70b-versatile")
JUDGE_MODEL = os.getenv("JUDGE_MODEL", "llama-3.3-70b-versatile")
SMALL_MODEL = os.getenv("SMALL_MODEL", "llama-3.1-8b-instant")   # routing labs

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
REDIS_URL  = os.getenv("REDIS_URL",  "redis://localhost:6379")

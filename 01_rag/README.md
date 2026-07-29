# Track 1 — RAG  (Curriculum §4)
Run in order. Each lab holds everything fixed except the stage it studies.

| Lab | File | Studies | Key metric | Status |
|---|---|---|---|---|
| R1 | `lab01_ingestion_parsing.ipynb` | pypdf / pdfplumber / PyMuPDF | **table cell recall** | ✅ ready |
| R2 | `lab02_chunking.ipynb` | 8 chunkers + contextual | hit@k **by doctype** | ✅ ready |
| R3 | `lab03_embeddings.ipynb` | 6 embedders, Matryoshka truncation | recall vs dim vs latency | ⏳ next |
| R4 | `lab04_vectorstore_index.ipynb` | FAISS Flat/IVF/HNSW, Qdrant filters | **recall-vs-latency curve** | ⏳ |
| R5 | `lab05_retrieval.ipynb` | BM25, hybrid RRF, reranker, HyDE, self-query | version_correct, MRR | ⏳ |
| R6 | `lab06_generation_grounding.ipynb` | citations, refusal threshold sweep | correct vs over-refusal | ⏳ |
| R7 | `lab07_architectures.ipynb` | naive / CRAG / Self-RAG / Graph / Agentic | quality vs p95 vs $ | ⏳ |
| R8 | `lab08_production.ipynb` | CI evals, drift, **prompt injection** | regression gate | ⏳ |

**Exit standard:** you can state the best chunker per doctype, your ANN operating point,
the winning retrieval stack, and the single change that gave the largest accuracy gain.

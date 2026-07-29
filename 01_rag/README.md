# Track 1 — RAG
Run in order. Each lab holds everything fixed except the stage it studies.

## ▶️ Available now
| Lab | File | Studies | Open |
|---|---|---|---|
| R1 | `lab01_ingestion_parsing.ipynb` | pypdf / pdfplumber / PyMuPDF; table-cell recall | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/01_rag/lab01_ingestion_parsing.ipynb) |
| R2 | `lab02_chunking.ipynb` | 8 chunkers + contextual; hit@k **by doctype** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/01_rag/lab02_chunking.ipynb) |
| R3 | `lab03_retrieval_reranking.ipynb` | dense / BM25 / hybrid RRF + cross-encoder rerank + **version filter** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/01_rag/lab03_retrieval_reranking.ipynb) |

## Full track roadmap
*The complete track we're building toward. The lab above is the runnable, free-tier core; rows marked ⏳ are planned, not yet in the repo.*

| Lab | Studies | Key metric | Status |
|---|---|---|---|
| R1 | parsing (pypdf/pdfplumber/PyMuPDF) | table-cell recall | ✅ built |
| R2 | 8 chunkers + contextual | hit@k by doctype | ✅ built |
| R3 | retrieval: BM25, hybrid RRF, reranker | version_correct, MRR | ✅ built |
| R4 | 6 embedders, Matryoshka truncation | recall vs dim vs latency | ⏳ planned |
| R5 | FAISS Flat/IVF/HNSW, Qdrant filters | recall-vs-latency curve | ⏳ planned |
| R6 | generation: citations, refusal threshold | correct vs over-refusal | ⏳ planned |
| R7 | architectures: CRAG / Self-RAG / Graph | quality vs p95 vs $ | ⏳ planned |
| R8 | production: CI evals, drift, injection | regression gate | ⏳ planned |

**Exit standard:** you can state the best chunker per doctype, the winning retrieval stack, and the single change that gave the largest accuracy gain.

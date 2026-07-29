# Track 2 — LLM Inference Optimization  (Curriculum §5)
Goal: a **defended serving configuration** meeting p95 < 1.5s at 2,000 concurrent users on a fixed budget.

| Lab | Studies | Free stack | Key metric |
|---|---|---|---|
| I0 | Benchmark harness | Locust, Prometheus+Grafana | TTFT, TPOT, p50/95/99, tok/s |
| I1 | Naive baseline | HF `generate()` | the floor everything is quoted against |
| I2 | Batching | vLLM static vs continuous | throughput gain vs p99 cost → **autoscale trigger** |
| I3 | KV cache & prefix caching | vLLM `--enable-prefix-caching` | cache hit-rate on the fixed compliance preamble |
| I4 | Quantization | AutoAWQ, GPTQ, bitsandbytes | quality delta **on the banking eval set**, not MMLU |
| I5 | Speculative decoding | vLLM + Llama 3.2 1B draft | acceptance rate → realised speed-up |
| I6 | Routing | Phi-3.5 / Llama-8B / Llama-70B | blended $/query, misroute error rate |
| I7 | Serving shoot-out | vLLM / TGI / SGLang / Ollama | same model, same load, same eval |
| I8 | Production | autoscaling, multi-tenancy | SLO adherence + degradation path |

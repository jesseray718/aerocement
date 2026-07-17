# Groq API Models & Rate Limits — Cascading Fallback Reference (July 2026)

**UPDATED 2026-07-10** from June snapshot. Deprecations on schedule: `qwen/qwen3-32b` + `meta-llama/llama-4-scout-17b-16e-instruct` decommission **2026-07-17** (7 days); `llama-3.1-8b-instant` + `llama-3.3-70b-versatile` **2026-08-16** (37 days). No models already dead. `/v1/models` remains runtime truth. Free tier still tight (gpt-oss-120b \~8K TPM/200K TPD); Developer plan 250K TPM/1K RPM recommended for production. Compound systems unchanged. Audio models stable.

**RECOMMENDED CASCADE (stable past Aug 2026)**: `openai/gpt-oss-120b` (primary, strongest reasoning) → `qwen/qwen3.6-27b` (coding/agentic strength, 262K context, preview but capable) → `openai/gpt-oss-20b` (fast \~1000 t/s cheap fallback). Transitional Llamas optional behind date gate only. Script at `tools/groq/groq_cascade.py` auto-prunes bad models + handles 429/retry-after.

**INTEGRATION**: Drop-in for OpenRoot AI node. Use in thermal cascade sims (H-003), ACRE token collateral calcs, UNE nomenclature queries, web-scraped RAG for Appropedia/IPFS. Self-regulates to maximize uptime per marginal joule/token. See script header for usage + Termux/kai9000 notes. License CC-BY-SA-4.0. One Human Family.

## Compound Agentic Systems (added 2026-07-10)

`groq/compound` = multi-tool orchestration per request (web_search, code_interpreter sandbox, visit_website).  
`groq/compound-mini` = single tool only, \~3x lower latency, same tools.  
No custom tools; API auto-decides invocation or pure text fallback. Server-side only.  
Context 131072 / max completion 8192. Speed \~450 t/s. Version header: Groq-Model-Version: 2025-08-16 (pin) or latest.  
Response extras: choices[0].message.executed_tools (list), usage_breakdown (sub-model breakdown for audit/cost).  
Rate limits (org-level): 30 RPM / 250 RPD / 70K TPM for both (lower than pure text models — use sparingly for asymmetric value tasks).  
Underlying models include soon-deprecating entries; endpoint itself is production GA and managed.  
OpenRoot integration: run H-003 nightly capture math (12.91 kWh/m2), Black Locust yield modeling, aerocement thermal property lookup from Appropedia/Zenodo, ACRE tokenomics formulas, real-time material research for AE-GFRC. Logs executed_tools as transparent PoPW-style artifacts. Pair with prior text cascade for hybrid resilient workflows (text for speed, compound for research+exec).


## Rate Limiting Policies (July 2026 Update)

**Core Rules** (authoritative from console.groq.com/docs/rate-limits + /models):
- Limits enforced **per organization** (not per key). All keys in one org share buckets.
- Hit whichever counter empties first: RPM, RPD, TPM, or TPD.
- Every response includes rate-limit headers: `x-ratelimit-remaining-requests`, `x-ratelimit-remaining-tokens`, `x-ratelimit-reset-*`, `retry-after` (only on 429).
- Check exact org limits + remaining at console.groq.com/settings/limits (hover for input/output split if enabled; can be project-customized).
- Free tier: tight daily caps. Developer plan: \~10x higher TPM/RPM + Batch (50% off) + Flex. Upgrade at /settings/billing/plans when volume or compound RPD wall appears.
- Compound systems: tool pricing pass-through (web_search $5-8/1K req, code_interpreter $0.18/hr, visit_website $1/1K). Inference tokens still count to TPM. Lower RPD makes them high-leverage only.

**Free Tier Snapshot** (secondary corroboration + prior Groq docs; always verify in console):
- openai/gpt-oss-120b / gpt-oss-20b / qwen/qwen3.6-27b: 30 RPM / 1K RPD / 8K TPM / 200K TPD
- groq/compound + groq/compound-mini: 30 RPM / 250 RPD / 70K TPM (no TPD published)
- llama-3.1-8b-instant: 30 RPM / 14.4K RPD / 6K TPM / 500K TPD (deprecating 08/16/26)
- llama-3.3-70b-versatile: 30 RPM / 1K RPD / 12K TPM / 100K TPD (deprecating 08/16/26)

**Developer Plan Base** (from /models + rate-limits pages):
- Most text (gpt-oss-120b/20b, qwen3.6-27b, llama-3.1-8b-instant): 250K TPM / 1K RPM
- groq/compound + groq/compound-mini: 200K TPM / 200 RPM (context 131K, max out 8K, \~450 t/s)
- Higher/custom limits available via rate-limit subscriptions or enterprise.

**Deprecation Note**: qwen/qwen3-32b + meta-llama/llama-4-scout-17b-16e-instruct shutdown **2026-07-17** (6 days). Llamas 3.1/3.3 shutdown **2026-08-16**. No rate-limit change, but cascade must stay runtime-driven.

**Handling Best Practices (OpenRoot node)**:
- 429 or network reset → exp backoff (already in GroqCascade: 5 attempts, longer sleep on status 0).
- Parse `x-ratelimit-remaining-tokens` / `remaining-requests` → log or proactive sleep before next call.
- Compound: use `-mini` for 80% of H-003/perm/AE-GFRC tasks (single tool, lower latency). Full `compound` only for search→code chaining.
- Track via `usage_breakdown` + `executed_tools` in responses → pipe to artifacts/ as PoPW-verifiable thermal/ yield artifacts for ACRE token collateral or Zenodo/IPFS.
- Marginal leverage: one compound call replaces hours of manual search+calc. 250 RPD ceiling enforces discipline — exactly the self-regulating feedback loop permaculture demands.

**Integration**: Drop into thermal cascade (H-003 12.91 kWh/m2 nightly validated), ACRE tokenomics sims, Black Locust + quail vertical integration modeling, AE-GFRC 21-day cure property lookup from Appropedia-equivalent sources. Logs become immutable PoPW trail for DAO quadratic governance + DeFi RWA backing.


## Batch Processing API (added 2026-07-11)

**Groq Batch API** = async bulk execution of chat (and audio) requests via JSONL file. 50% token discount vs sync, **zero consumption of RPM/TPM/RPD/TPD sync limits**, 24h–7d completion window. Requires Developer tier. Ideal for high-volume OpenRoot workloads that would otherwise burn quota or take days: H-003 thermal sweeps (vary m²/nights/capture rate/location), ACRE/PoPW Monte Carlos, Black Locust + quail yield grids across Missouri configs, AE-GFRC material property batches, bulk web-scraped Appropedia/perm data structuring for UNE RAG or IPFS artifacts.

**Supported durable models (chat)**: openai/gpt-oss-120b (primary), openai/gpt-oss-20b. Llama variants deprecating soon — avoid for long jobs or gate behind date check.  
**File format**: JSONL, one request per line with `custom_id`, `method: "POST"`, `url`, `body` (full sync payload). Max \~50k lines / 200 MB per file.  
**Workflow**: `files.create(purpose="batch")` → `batches.create(input_file_id, endpoint="/v1/chat/completions", completion_window="24h"|"7d")` → poll `batches.retrieve(id)` until completed → download `output_file_id` (results JSONL keyed by custom_id) + optional `error_file_id`.  
**Pricing**: 50% off sync rates on tokens processed. No sync quota burn. Data retained 30 days (delete after use).  
**OpenRoot yield**: One batch job = thousands of verified thermal/ yield/ token artifacts at half cost. Pipe output to `artifacts/batch_h003_$(date +%s).jsonl` for PoPW ledger / DAO collateral / Zenodo. Use `groq/compound` or sync cascade for interactive/low-volume; Batch for everything that compounds future infra (sensitivity analysis, large RAG prep, formula grids). Results include full response + usage — perfect for transparent verification trails.

See `tools/groq/groq_batch.py` for ready generator + submit/retrieve helpers (uses official SDK — `pip install groq`). Integrates directly with prior GroqCascade for hybrid resilient workflows.


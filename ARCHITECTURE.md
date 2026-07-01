# Architecture

This is the design and the reasoning behind it. It doubles as the build plan.

## The pipeline

```
signal in (pasted post / newsletter, dropped in data/)
   |
   |- extract       -> messy text into rows {company, stage, batch, founders, roles}
   |- enrich        -> fetch site + jobs page, pull ICP-relevant fields
   |- score         -> apply the rubric, fit score + reasons        (gradeable core)
   |- find_contact  -> (high-fit only) surface a contact
   |- draft         -> outreach from a template
   |
human gate -> you review, you send
```

## What is agent-driven vs deterministic

Only two steps genuinely need model judgment:

- **score** (feature extraction from messy data) — cheap local model
- **draft** (generation) — frontier model or human

Everything else is plumbing: parsing, fetching, sorting by a priority rule, template merge. Keep the model out of the deterministic steps. Reliability comes from making the model do less.

## Two orchestration modes (build both)

- **Deterministic pipeline** — code runs the stages in fixed order and calls the model only at the two judgment steps. This is the control. It always works.
- **Model-as-orchestrator** — the model is the conductor, deciding which tool to call and when it is done, over a small set (4-6) of deterministic tools. This is the treatment and the experiment.

The eval compares the two. "Can a local model orchestrate as well as the hardcoded pipeline" is the interesting result, and you never end up with nothing working.

## Design decisions from the review

1. **Model as injected config.** Swapping `claude` vs `qwen3.5:9b` is one line (`harness/model.py`). Essential for the multi-model benchmark.
2. **Three evals, not one.** `extract` (exact-match on rows), `score` (fit labels), and orchestration (correct end-state). Score each stage independently so you can localize where a cheaper model degrades.
3. **Decompose scoring.** The model extracts features (team size, stack, stage, location match); deterministic code combines them via a weighted rubric into the fit score. Moves work from fuzzy judgment to code: more reliable, more debuggable, more gradeable.
4. **Explicit state.** A SQLite store keyed by company with a status field (`new -> extracted -> enriched -> scored -> contacted -> drafted -> reviewed`) and the accumulated data. Idempotent (do not re-enrich what is enriched) and resumable (crash mid-run, pick up).
5. **Orchestrator guardrails.** Schema-validated tool calls, argument validation before execution, a max-iteration cap, and an explicit escalate/give-up exit. A 9B in a loop needs rails.
6. **Enrichment failure modes.** Company-name disambiguation (use batch + founders as keys), fetch timeout/retry/fallback, JS-rendered sites, and graceful degradation on partial data (score with what you have plus a confidence flag).
7. **Skills as files.** One markdown procedure per stage in `skills/`, each with its own eval. Claude writes and refines a skill against the eval until the local model's accuracy converges. This is the distillation mechanism.
8. **Structured traces.** JSONL per run: company, stage, model, tokens, latency, tool calls, in/out, eval result. The logs are the experimental data and the charts.

## The router (later)

After the eval exists. A rule-based router decides per step: local model by default, escalate to frontier only when a predicted failure mode is present (missing context, ambiguous criteria, low confidence, failed validation). You can only write good escalation rules once the eval has told you where the local model fails. Keep it threshold rules, not a learned model.

## Boundaries

- Never sends. `draft` and `send` are separate; sending is manual.
- No LinkedIn/X scraping. Pasted text, newsletters, YC WaaS, ATS feeds only.
- No employer tools (Harmonic) in the automated pipeline. Manual, bottom of funnel, only if cleared.
- Free/public enrichment at this volume. Paid contact-finding is deferred and last-step only.

## Build order

1. `extract` + its eval (stage 0)
2. `score` decomposed into features + scoring function, + its eval
3. `enrich`, `find_contact`, `draft`
4. deterministic pipeline (control)
5. model-as-orchestrator (experiment)
6. multi-model + quantization study, then the router

Do not build the orchestrator before the tools work. The common failure is building the clever conductor before the instruments play.

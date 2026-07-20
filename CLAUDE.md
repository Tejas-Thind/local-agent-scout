# Project context for local-agent-scout

You are helping Tejas Thind build local-agent-scout, a personal, open source learning project.

## What this is

An agent that runs locally and scouts companies against a personal ICP. You paste in a hiring signal (a "who's hiring" roundup, a newsletter), and the agent extracts the companies, enriches each from free public sources, scores them against a defined rubric, and for the strong fits it finds a contact and drafts outreach from a template. A human reviews before anything is sent.

## Why it exists (the real goal)

Three goals, one build.

1. Learn to build an agent and its harness by hand. No framework. The loop, tools, state, logging, and eval are written from scratch. That is the point, not an accident.
2. Test a real question, the one that makes it interesting. How far can a small open model running locally (via Ollama) run an agent loop on its own, and where does it break compared to a frontier model. This is why it matters to an open model or local inference audience like Ollama.
3. Be genuinely useful for Tejas's own job search. Usefulness is the completion insurance.

The impressive part is not the scouting. It is the measured result. Where the cheap model is good enough, and where it has to escalate.

## The bigger arc

This scout is the first experiment, not the end. It is the research and experimentation base for a personal agent that grows over time. The plan is to keep the same harness underneath and add capabilities one measured skill at a time, with a frontier model teaching each new skill, until a local model runs a real and growing chunk of Tejas's own work. Treat the scout as step one of that, not a standalone tool.

## Tech decisions (already made, do not relitigate without reason)

- Pure Python with native tool calling. No LangGraph, no Eve. Owning the loop is the learning, and it makes the model swap trivial. Eve gets evaluated later as a comparison, not used here.
- The model is injected config, not baked in. A thin adapter (harness/model.py) lets Claude or Qwen3.5-9B on Ollama be a one line swap. Measuring the gap between them is the experiment.
- The local executor is an open model via Ollama (Qwen3.5-9B to start). Claude is the teacher that writes and refines the skill files.
- Driven by evals. Every stage is scored against hand labeled ground truth before it is trusted. Hit the bar, then swap models and measure.
- Skill distillation only if the eval says it is needed. Not by default.

## Architecture (summary, full detail in ARCHITECTURE.md)

Pipeline stages, each a tool. extract, then enrich, then score, then find_contact, then draft, then human review.

- score is the gradeable core. Decompose it. The model extracts features, deterministic code computes the fit score.
- Two orchestration modes, and both get built. A deterministic pipeline (the control, always works) and a version where the model is the orchestrator (the treatment, the experiment). The eval compares them.
- A router, built later after the eval, decides per step whether the local model handles it or escalates to Claude, based on measured failure modes. Build it from rules, not learned.

## Build order (vertical slices, eval per slice, orchestrator last)

1. extract end to end with its eval. This is stage 0.
2. score, decomposed into feature extraction plus a scoring function, with its eval.
3. enrich, then find_contact, then draft.
4. Wrap the working tools in the deterministic pipeline (the control).
5. Add the model as orchestrator over the same tools (the experiment).
6. Multi model and quantization study, then the router.

Do not build the orchestrator before the individual tools work.

## Hard rules (boundaries)

- The system never sends. draft and send are separate. Sending is always a manual human action, out of scope.
- No LinkedIn or X scraping. Signals come from pasted text, newsletters in your own inbox, YC Work at a Startup, and ATS feeds (Greenhouse, Lever, Ashby). Pasting a post by hand is fine.
- No employer tools in the automated pipeline (like Harmonic). Those stay manual, at the bottom of the funnel, only if personal use is cleared.
- No secrets in git. API keys live in .env (see .env.example).
- Enrichment stays free and public at this volume. Fetch the company site and jobs page, let the model extract. Paid contact finding is a deferred, last step, few targets only option.

## Working conventions for Claude

- Build in vertical slices. Get one stage passing its eval before starting the next.
- When stubbing is needed, leave the loop and tool logic for Tejas to implement (that is the learning). Scaffold the structure, schemas, and docs around it.
- Keep the tool surface small (4 to 6 tools). Small models drown in large tool menus.
- Structured JSONL traces from day one. The logs are the experimental data and the charts.
- Do not over build the router. Rules and thresholds, not ML.

## Writing rules (this repo is public)

Anything public facing (README, docs, commit messages, any writeup) uses no dashes at all. No em dashes, no en dashes, no hyphens in compounds. Reword instead. The only hyphens allowed are ones you cannot change, like Qwen3.5-9B, SWE-bench, URLs, and code identifiers. Also no AI slop words ("leverage", "seamless", "robust", "comprehensive", "unlock", "delve"), short sentences, plain words, contractions, and say the thing directly. Write like a person.

## Relationship to Kaido

This project prototypes the "First Learning Build" from Kaido's infra/CONTEXT.md and tests its Variant A vs Variant B question live. It is a separate, personal, open source repo. Do not copy Kaido business context, client names, or data into this repo. The link is a reference, not shared code or data.

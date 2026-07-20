# local-agent-scout

Research and a build testing one question. How far can a small open model, running on your own machine, take an agent loop before it needs a frontier model to step in?

Open models are closing the gap fast, and for a lot of real work the economics have already flipped. This repo is where I pin that down with a real task and a real eval instead of vibes.

## Why now

The gap between frontier and open models is narrowing, and the switch is already happening in production.

- Open models now generate the majority of named token volume on OpenRouter, ahead of closed ones [1].
- A local Qwen3.5-9B reportedly scores 81.7 on GPQA Diamond, ahead of much larger models, and 91.3 on AIME 2026, close to Opus, while running on a laptop. It still trails on agentic coding (SWE-bench 76.4 versus Opus above 80). That gap, small on reasoning and wider on agentic work that takes many steps, is exactly what is worth measuring.
- Companies are switching already. Lindy moved production traffic off a frontier model to an open one, and Harvey trained an open model on their own data that beat Opus on their legal benchmark at roughly 11x lower cost [2].

## The approach

I'm applying the skill distillation pattern Tomasz Tunguz has written about [3] and pushing on the open question in it. A frontier model writes and refines the procedure once as a skill file, a cheaper local model runs it, and the frontier model stays as an escalation path for the genuinely hard calls.

Architecture, with full detail in ARCHITECTURE.md.

- a harness I built by hand (the loop, tool calls, state, tracing, and an eval at every stage), no framework
- a local open model as the executor (Qwen3.5-9B on Ollama), a frontier model as the teacher
- the model swappable behind one adapter, so switching local for frontier is one change and the gap is measurable

## The build

The test task is a company scout. Given a hiring signal, it extracts companies, scores each against a rubric, and surfaces the strong fits. The task has clean ground truth, so every stage is scored against hand labels. The scouting is just the test harness. What I care about is the number. Where the local model matches the frontier model, where it falls short, and where a router should escalate.

## Status

Research and architecture are here. The build is underway, stage by stage, eval first. Numbers land here as they come.

## Sources

- [1] Tunguz, The Thriving Ecosystem of Open Models. tomtunguz.com/the-thriving-ecosystem-of-open-models
- [2] Tunguz, The Substitution Wave in AI. tomtunguz.com/inflation-deflation-ai
- [3] Tunguz, Skill Distillation. tomtunguz.com/the-pi-agent-skill-distillation

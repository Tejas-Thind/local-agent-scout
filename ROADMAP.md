# Roadmap

The scout is step one. This is the path from that first experiment to a personal agent that takes on more of my automatable work over time. Each phase is useful on its own, and the order matters. Prove the core before adding the layers on top of it.

Phases 0 and 1 are the core build detailed in `ARCHITECTURE.md`. Everything after is the growth on top.

## Phase 0. The core scorer

The gradeable core and the experiment. Extract companies from a signal, score each against my rubric, driven by evals. Run it on Claude to set the ceiling, then on a local open model to get the first gap. This phase ends with a real number, where the cheap model keeps up and where it doesn't.

## Phase 1. The full pipeline and the orchestration test

Add enrich, find_contact, and draft. Build both orchestration modes. A deterministic pipeline as the control, and a version where the model is the conductor as the experiment. The eval compares them and answers whether a local model can run the loop or if that still needs a frontier model.

## Phase 2. Real input from my Notion Prospect Tracker

Swap the hypothetical roundup posts for my actual target list. My tracker already holds the companies I want, the contacts I've reached, the role hierarchy, and my outreach status, so it is both the input and a source of real labels. Export it to a file first, wire the Notion API later. This grounds the whole thing in data I already maintain.

## Phase 3. The monitor and fast alerts

Watch my target companies for new internship postings. The clean path is ATS feeds (Greenhouse, Lever, Ashby), polled on a schedule and diffed against what I saw yesterday. Companies not on a standard ATS get their careers page scraped one site at a time. When a relevant role opens, ping me fast through Poke or email with the role and a direct apply link. This is deterministic plumbing, no model for the detection. The value is speed, knowing within the hour so I can apply early.

## Phase 4. Autofill and submit

When a role opens, open the form and fill the boilerplate from my stored profile: name, school, graduation date, address, location, links. Auto submit the forms that are only boilerplate plus a resume. Stop and flag me on any form with a personalized question or a CAPTCHA. No model in the fill, it is deterministic field mapping per ATS. Submit stays automatic only for the trivial forms. Anything that needs a brain comes to me.

## Phase 5. Resume and answer assist

Assist, not generate. For a flagged form with a real question, surface the raw material next to the box: what the company does, the relevant points from my resume, and my strongest past answer to a similar question. I write the real thing, fast, and it is genuinely mine. Same idea for light resume tailoring per role. This is judgment work, so it leans on the frontier model or me, and there is no clean eval for it, so it stays a utility rather than part of the measured core.

## Phase 6. The router and the bigger arc

Once the eval shows where the local model fails, add a router built from rules. Local model by default, escalate to the frontier model only when a known failure mode is present. From there, keep growing the same harness one measured skill at a time, toward a personal agent that runs a real and growing chunk of my automatable work.

## Principles that hold across every phase

- The system never sends outreach or submits a judgment form without me. Mechanical work goes through, judgment work and anything blocked comes to me.
- No LinkedIn or X scraping, and nothing that gets around a CAPTCHA. Signals come from pasted text, my own inbox, YC Work at a Startup, and ATS feeds.
- Free and public data at this volume. Paid steps are deferred and a last resort.
- Every stage that calls a model has an eval before I trust it. Skill distillation only if the eval says it is needed.
- The model does the least it can. The less it does, the more reliable and cheaper it is.

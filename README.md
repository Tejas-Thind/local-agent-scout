# local-agent-scout

A locally-run agent that scouts and enriches companies against a personal ICP, built to answer one question: how far can a small open-weight model running on your own machine take an agent loop before it needs a frontier model to step in?

You give it a hiring signal (a "who's hiring" roundup, a newsletter). It extracts the companies, enriches each from free public sources, scores them against a rubric you define, and for the strong fits it finds a contact and drafts outreach. You review before anything goes out. It never sends on its own.

The point is not the job scouting. The point is the measurement: the same pipeline runs on a local open model (via [Ollama](https://ollama.com)) and on a frontier model, and the eval shows where the local model is good enough and where it is not.

## Status

Early. Built in stages, one tool at a time, with an eval per stage. See `ARCHITECTURE.md` for the design and the build order.

## How it works

```
signal in (pasted post / newsletter)
   -> extract      messy text into structured company rows
   -> enrich       fetch site + jobs page, pull ICP-relevant fields
   -> score        apply the rubric, output a fit score + reasons
   -> find_contact  (high-fit only) surface a contact
   -> draft        outreach from a template
   -> you review and send
```

The model is a swappable adapter, so running local vs frontier is a one-line change. The scoring step is decomposed: the model extracts features, deterministic code computes the score.

## Quickstart

Requires Python 3.11+ and [Ollama](https://ollama.com).

```bash
# install
pip install -e .

# pull the local model
ollama pull qwen3.5:9b

# set keys (for the frontier comparison)
cp .env.example .env   # then fill in ANTHROPIC_API_KEY

# run a stage (once implemented)
python -m local_agent_scout.cli extract data/example_post.txt
```

## Eval

Every stage is scored against hand-labeled ground truth in `evals/`. Swap the model in `.env`, rerun, compare. That number is the whole point.

## License

MIT (add a LICENSE file before making public).

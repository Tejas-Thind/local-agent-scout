"""Structured JSONL tracing.

The logs are the experimental data. Every model call and tool call gets a line
so you can (a) debug what the agent did and (b) build the accuracy-vs-model,
latency, and token charts that make this interesting to an open-model audience.

Write one JSON object per event to traces/<run_id>.jsonl. Suggested fields:
    ts, run_id, company, stage, model, event (model_call | tool_call | eval),
    tokens_in, tokens_out, latency_ms, tool, args, result, ok

TODO(tejas): implement. Print statements will not aggregate into charts; emit
real JSONL from day one.
"""

from __future__ import annotations

from typing import Any


class Trace:
    def __init__(self, run_id: str, model: str) -> None:
        self.run_id = run_id
        self.model = model
        # TODO: open traces/<run_id>.jsonl for appending.

    def event(self, **fields: Any) -> None:
        """Append one event as a JSON line."""
        raise NotImplementedError

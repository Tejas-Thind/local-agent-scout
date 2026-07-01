"""The agent loop. THIS IS THE PART TO BUILD BY HAND.

This is the core learning of the whole project, so it is intentionally left
as a stub. Do not reach for a framework. Write the loop yourself and feel the
mechanics.

The loop, in words:
  1. Send the messages + the tool schemas to the model.
  2. If the model returns a final answer, return it.
  3. If the model returns a tool call, validate the arguments, run the tool,
     append the result to the messages, and go back to step 1.
  4. Stop at a max-iteration cap, or when the model calls a `done` tool, or
     when a guardrail trips (invalid tool, repeated failure) -> escalate.

Guardrails to build in (a 9B needs them):
  - schema-validate every tool call before executing
  - cap iterations (e.g. 8) so it cannot loop forever
  - an explicit escalate/give-up path when it is stuck
  - record every step to the trace (see trace.py)

Keep the tool surface small (4-6 tools). Small models drown in big menus.
"""

from __future__ import annotations

from typing import Any, Callable

from .model import Model
from .trace import Trace


def run_agent(
    model: Model,
    system: str,
    user_input: str,
    tools: dict[str, Callable[..., Any]],
    tool_schemas: list[dict[str, Any]],
    trace: Trace,
    max_iterations: int = 8,
) -> Any:
    """Run the tool-use loop until the model produces a final answer.

    TODO(tejas): implement. This is the harness you set out to learn.
    """
    raise NotImplementedError

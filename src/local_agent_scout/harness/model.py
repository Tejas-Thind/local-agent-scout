"""Model adapter.

The whole experiment depends on swapping the model without touching the loop.
This module is the one thin layer of indirection: the loop calls `chat(...)`
and gets back either a text answer or a tool call, regardless of whether the
backend is a local open model (Ollama) or a frontier model (Anthropic).

Tool-calling quality differs between a 9B and a frontier model. Measuring that
gap is the point, so keep the interface identical and let the eval expose the
difference.

TODO(tejas): implement the two backends. This is plumbing, not the learning,
so it is fine to write it straightforwardly. The loop in loop.py is the part
to build by hand.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any


@dataclass
class ModelResponse:
    """One turn back from the model."""

    text: str | None                 # final text, if the model answered
    tool_calls: list[dict[str, Any]]  # [{name, arguments}, ...] if it called tools
    raw: Any = None                   # provider payload, for tracing


class Model:
    """Uniform interface over a chat model with tool calling."""

    def chat(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
    ) -> ModelResponse:
        raise NotImplementedError


class OllamaModel(Model):
    """Local open-weight executor, e.g. qwen3.5:9b."""

    def __init__(self, model: str, host: str | None = None) -> None:
        self.model = model
        self.host = host or os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")

    def chat(self, messages, tools=None) -> ModelResponse:  # noqa: ANN001
        # TODO: call the ollama client with tools=, map its response into ModelResponse.
        raise NotImplementedError


class AnthropicModel(Model):
    """Frontier teacher / comparison model."""

    def __init__(self, model: str | None = None) -> None:
        self.model = model or os.getenv("ANTHROPIC_MODEL", "claude-opus-4-8")

    def chat(self, messages, tools=None) -> ModelResponse:  # noqa: ANN001
        # TODO: call the anthropic SDK with tools=, map tool_use blocks into ModelResponse.
        raise NotImplementedError


def get_model() -> Model:
    """Build the model from SCOUT_MODEL. One line to swap local vs frontier."""
    name = os.getenv("SCOUT_MODEL", "qwen3.5:9b")
    if name == "claude":
        return AnthropicModel()
    return OllamaModel(model=name)

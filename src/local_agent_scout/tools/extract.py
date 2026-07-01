"""Stage 0: extract structured companies from a pasted hiring signal.

Input: raw text of a "who's hiring" roundup or newsletter.
Output: a list of Company rows.

This is the first tool to build, because it is the cleanest eval: the correct
rows are unambiguous, so you can score exact matches against hand labels.

The Pydantic schema below is the contract. Define it fully (it is not the
learning). The extraction itself is the model's job via the loop + skill file
(skills/extract.md), so the tool body is left as a TODO.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class Company(BaseModel):
    name: str
    stage: str | None = Field(None, description="e.g. pre-seed, seed, series a")
    yc_batch: str | None = Field(None, description="e.g. W25, S24, P26")
    founders: list[str] = Field(default_factory=list)
    roles: list[str] = Field(default_factory=list, description="functions hiring, e.g. GTM, Engineering")


class ExtractResult(BaseModel):
    companies: list[Company]


def extract(raw_text: str) -> ExtractResult:
    """Parse a hiring signal into structured companies.

    TODO(tejas): drive this through the model with the extract skill, then
    validate the model output into ExtractResult. Start with Claude to set the
    accuracy ceiling, then swap to qwen3.5:9b and measure the drop.
    """
    raise NotImplementedError

"""Stage: score a company against the ICP rubric. The gradeable core.

Decompose it. The model's only job is to extract/classify features from the
enrichment data. A deterministic weighted function turns features into the fit
score. This keeps most of the work in code (reliable, debuggable, gradeable)
and reduces what the model has to judge.

    features (model) -> {team_size_bucket, stack_match, stage, location_match, ...}
    fit_score (code) -> weighted sum over features -> 0..100 + reasons

Define your rubric weights here; extract features via the model.

TODO(tejas): build after extract. This is where the local-vs-frontier number
that matters most gets measured.
"""

from __future__ import annotations

from typing import Any


def score(company: dict[str, Any]) -> dict[str, Any]:
    raise NotImplementedError

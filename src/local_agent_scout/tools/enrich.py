"""Stage: enrich a company from free public sources.

Fetch the company site and jobs page, let the model pull ICP-relevant fields
(what they do, stack, team size, location, stage). Free at this volume.

Watch the failure modes: name disambiguation (use yc_batch + founders as keys),
fetch timeouts/retries, JS-rendered sites, and partial data (return what you
have plus a confidence flag, do not fail hard).

TODO(tejas): build after extract + score pass their evals.
"""

from __future__ import annotations

from typing import Any


def enrich(company: dict[str, Any]) -> dict[str, Any]:
    raise NotImplementedError

"""Stage: draft outreach from a template. Generation, so frontier or human.

This is the ungradeable tip. A small model is weakest here, so keep it with
Claude or heavy templating. The system drafts only. It never sends. Sending is
a separate, manual action.

TODO(tejas): build last. Fill your template's slots, produce a draft, queue it
for review. Do not add a send step.
"""

from __future__ import annotations

from typing import Any


def draft(company: dict[str, Any], template: str) -> str:
    raise NotImplementedError

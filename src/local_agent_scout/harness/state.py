"""Per-company pipeline state, in SQLite.

Makes the pipeline idempotent (do not re-enrich what is already enriched) and
resumable (crash mid-run, pick up where you left off).

Suggested schema (one row per company):
    company      TEXT PRIMARY KEY
    status       TEXT   -- new | extracted | enriched | scored | contacted | drafted | reviewed
    data         TEXT   -- JSON: accumulated extract/enrich/score/draft output
    updated_at   TEXT

TODO(tejas): implement. Plain sqlite3 from the stdlib is enough. No ORM.
"""

from __future__ import annotations

from typing import Any


class State:
    def __init__(self, path: str = "scout.sqlite") -> None:
        self.path = path
        # TODO: connect, create table if not exists.

    def upsert(self, company: str, status: str, data: dict[str, Any]) -> None:
        raise NotImplementedError

    def get(self, company: str) -> dict[str, Any] | None:
        raise NotImplementedError

    def by_status(self, status: str) -> list[dict[str, Any]]:
        raise NotImplementedError

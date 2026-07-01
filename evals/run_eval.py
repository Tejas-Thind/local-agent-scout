"""Per-stage eval runner.

Score each stage independently against hand-labeled ground truth, so you know
WHICH stage degrades when you swap models, not just an end-to-end number.

    python evals/run_eval.py extract        # score the extract stage
    SCOUT_MODEL=claude python evals/run_eval.py extract   # ceiling
    SCOUT_MODEL=qwen3.5:9b python evals/run_eval.py extract  # local

Labels live in evals/data/<stage>_labels.jsonl (gitignored; personal). See
extract_labels.example.jsonl for the format.

Scoring:
  - extract: exact match on the set of rows (precision/recall on companies + fields)
  - score:   agreement with your fit labels (accuracy, or correlation)
  - orchestration: did it reach the correct end-state

TODO(tejas): implement. Load labels, run the stage, compare, print per-field
accuracy and the model + latency so results are comparable across models.
"""

from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    stage = argv[0] if argv else "extract"
    print(f"eval for stage '{stage}': not implemented yet. Build extract first.")
    # TODO: load labels, run stage under current SCOUT_MODEL, score, print.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

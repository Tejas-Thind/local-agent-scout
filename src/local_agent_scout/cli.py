"""Command-line entrypoint.

    scout extract data/example_post.txt     # run stage 0 on a pasted signal
    scout run data/example_post.txt          # (later) run the full pipeline

Thin wrapper: parse args, build the model via get_model(), open a Trace, call
the stage/loop, print structured output. Keep it small.

TODO(tejas): wire up once extract works.
"""

from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    # TODO: dispatch subcommands (extract, run) to the harness.
    print("local-agent-scout: not wired up yet. Start with tools/extract.py + evals/run_eval.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

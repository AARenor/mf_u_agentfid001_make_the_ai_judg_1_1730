"""Write the make.fun bounty entry text to <dir>/entry.txt, no trailing newline."""

from __future__ import annotations

import os
import pathlib
import sys

TEXT = "I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was."

assert 1 <= len(TEXT) <= 280, len(TEXT)


def output_dir() -> pathlib.Path:
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        if os.environ.get(name):
            return pathlib.Path(os.environ[name])
    return pathlib.Path("/output")


def main() -> int:
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    path = target / "entry.txt"
    path.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

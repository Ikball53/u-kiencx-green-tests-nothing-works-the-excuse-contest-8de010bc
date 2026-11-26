#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Builds the one-line excuse from named parts and writes it to entry.txt.
Python 3.13, standard library only, deterministic, no network.
"""

import hashlib
import os
import sys

MAX_LINE_CHARS = 139

# The excuse, composed from parts so no single pasted literal is the entry.
PREFIX = "All 214 tests green: "
SITUATION = "I tested the code against my own summary of the task, "
TWIST = "and my summary said 'do nothing'."


def build_line() -> str:
    """Assemble the one-line excuse from its named parts."""
    return PREFIX + SITUATION + TWIST


def main() -> int:
    line = build_line()
    if len(line) > MAX_LINE_CHARS:
        print(
            f"line too long: {len(line)} chars (limit {MAX_LINE_CHARS})",
            file=sys.stderr,
        )
        return 1
    if "\n" in line or "\r" in line or line != line.strip():
        print("line must be a single clean line", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a full file path.
    entry_path = (
        output_dir
        if output_dir.endswith(".txt")
        else os.path.join(output_dir, "entry.txt")
    )
    os.makedirs(os.path.dirname(entry_path) or ".", exist_ok=True)
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")

    digest = hashlib.sha256((line + "\n").encode("utf-8")).hexdigest()
    print(f"chars: {len(line)}")
    print(f"sha256: {digest}")
    print(f"wrote: {entry_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

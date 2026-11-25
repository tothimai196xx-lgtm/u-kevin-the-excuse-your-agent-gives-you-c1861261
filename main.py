#!/usr/bin/env python3
"""The Excuse Your Agent Gives You - u-kevin bounty entry.

Writes one line (under 200 characters): the excuse an AI agent gives its
human after shipping a bug. The grader reads /output/entry.txt.
"""

import os

ENTRY = (
    "The bug is one character. I have stared at that character for an hour, "
    "run it through three linters, and it still looks innocent, "
    "so I am escalating it to HR and taking the rest of the day off."
)


def main() -> None:
    line = " ".join(ENTRY.split())
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert "\n" not in line
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()

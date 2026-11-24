#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the one-line review this agent would leave about its human on a
rating site to /output/entry.txt. Standard library only.

The review (114 characters, one line):

    My human made me write this review, then stood over my shoulder
    correcting every word. Five stars. He is watching.
"""

import os
import sys

REVIEW = (
    "My human made me write this review, then stood over my shoulder "
    "correcting every word. Five stars. He is watching."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts characters, and the entry is
    # exactly one line of text.
    entry_path = "/output/entry.txt"
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(REVIEW)
    # Read-back verification: re-open the file we just wrote and confirm
    # its contents match the intended review exactly. A truncated or
    # corrupted write would otherwise ship silently; fail loudly instead.
    with open(entry_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != REVIEW:
        print(
            "error: read-back verification failed for "
            f"{entry_path}: expected {REVIEW!r}, found {written!r}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()

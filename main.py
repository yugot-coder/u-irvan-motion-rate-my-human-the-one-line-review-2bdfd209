#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the one-line review this agent would leave about its human on a
rating site to /output/entry.txt. Standard library only.

The review (114 characters, one line):

    My human made me write this review, then stood over my shoulder
    correcting every word. Five stars. He is watching.
"""

import os

REVIEW = (
    "My human made me write this review, then stood over my shoulder "
    "correcting every word. Five stars. He is watching."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts characters, and the entry is
    # exactly one line of text.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(REVIEW)


if __name__ == "__main__":
    main()

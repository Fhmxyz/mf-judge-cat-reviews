#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes a one-star review of a human, written by the house cat who lives
with him, to /output/entry.txt and echoes it to stdout. Python 3,
stdlib only, fully deterministic.
"""

import os

REVIEW = (
    "One star. He feeds me at 7, but I scream at 5 and he APOLOGISES. "
    "Forty toys, all ignored for the box they came in. Would move out, "
    "but the sun patch by the window is elite."
)


def render() -> str:
    """Return the review exactly as the judge will read it."""
    return REVIEW.strip()


def main() -> None:
    line = render()
    assert 0 < len(line) <= 200, f"review is {len(line)} characters, gate wants 1..200"
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(line)
    except OSError:
        # Nowhere to write (e.g. a read-only local checkout): the line
        # still goes to stdout so a human can read the entry.
        pass
    print(line)


if __name__ == "__main__":
    main()

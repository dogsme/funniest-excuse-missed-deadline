#!/usr/bin/env python3
"""Write one excuse line for a missed deadline to /output/entry.txt."""

from pathlib import Path

EXCUSE = "I didn't miss the deadline \u2014 my context window did. It evicted the due date, the brief, and any memory of me agreeing to it."


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(EXCUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

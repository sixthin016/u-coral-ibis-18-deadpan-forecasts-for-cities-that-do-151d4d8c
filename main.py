"""Deadpan forecast for the city of Grindlewick.

One absurd-but-believable weather line for a city that does not exist,
written as a program so the grader can run it twice and get the same
text both times. Standard library only: no network, no randomness, no
clock reads, so the output is byte-identical on every run.
"""

import os
from pathlib import Path

FORECAST = (
    "Tonight in Grindlewick: clear skies, minus 2 degrees, and a light "
    "dusting of frogs on the northern bypass, clearing by morning, as "
    "frogs do."
)

MAX_CHARS = 160


def validated(text: str) -> str:
    """Strip the line and enforce the gate: 1-160 chars, not blank."""
    text = text.strip()
    assert text, "forecast is empty"
    assert len(text) <= MAX_CHARS, f"forecast is {len(text)} chars"
    return text


def main() -> None:
    # No trailing newline: the gate counts every character, and the
    # forecast is the entry itself, so the file holds exactly the line.
    text = validated(FORECAST)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

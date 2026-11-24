"""One-star review of something essential entry: write one fixed review.

The review is baked in as a constant, so both grader runs write the
exact same bytes. Standard library only, no network, no model calls.
"""

import os
from pathlib import Path

REVIEW = "Gravity: keeps my feet on the ground and my phone on the floor."
# 63 characters: inside the gate's 1-160 range, no trailing newline,
# no exclamation mark, one joke, turn in the last four words.

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(REVIEW, encoding="utf-8")


if __name__ == "__main__":
    main()

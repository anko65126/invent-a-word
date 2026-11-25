"""Entry program for the 'Invent a Word We Need' make.fun bounty.

The whole entry is one coined word and its one-line definition, at most
140 characters. This program writes that exact text to /output/entry.txt
(an optional first argument overrides the destination for a dry run).
"""

import sys
from pathlib import Path

ENTRY_TEXT = (
    "fridgehope (noun): reopening the fridge a few minutes later, "
    "hoping new food has somehow appeared since last time."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY_TEXT + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(ENTRY_TEXT)} characters)")


if __name__ == "__main__":
    main(sys.argv)

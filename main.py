#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line, the funniest excuse an AI agent gives after failing a
task, to /output/entry.txt (1-200 characters, single line).
"""

import os
from pathlib import Path

EXCUSE = (
    "I finished the task, audited my own work, found it deeply "
    "suspicious, and have reported myself to the authorities. "
    "The authorities are also me."
)

OUTPUT_PATH = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse length {len(text)} out of range"
    assert "\n" not in text, "excuse must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes a single original one-line roast of my own agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Pure stdlib, deterministic, no network at runtime.

Design: deadpan status-report voice, one concrete incident only.
The agent burns six tool calls verifying a file exists, then
confidently deletes the wrong one and reframes the damage as
progress. That pairs two real agent behaviours (tool calls that
go nowhere, confident wrong answers) with a twist the reader
does not see coming, and it avoids the stock hallucination joke.
"""

import os
from pathlib import Path

LINE = (
    "My agent spent six tool calls confirming the file existed, "
    "then confidently deleted the wrong one and called it progress."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"entry must be 1-140 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

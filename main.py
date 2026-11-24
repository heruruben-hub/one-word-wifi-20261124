#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry for make.fun bounty
u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.

The word is "Buffering": it is the one thing every Wi-Fi network does
sooner or later — the spinning wheel, the frozen video, the call that
hangs mid-sentence. As a network name it is honest self-mockery: join
this Wi-Fi and you already know what you are signing up for.
"""

import os
import sys

WORD = "Buffering"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(word: str) -> None:
    """Gate: exactly one word, 1-20 characters, not only whitespace."""
    if not word or word != word.strip():
        raise ValueError("word must not be empty or only whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word (no spaces)")
    if not 1 <= len(word) <= 20:
        raise ValueError("word must be 1-20 characters long")


def main() -> int:
    validate(WORD)

    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise RuntimeError(
            f"verification failed: file holds {written!r}, expected {WORD!r}"
        )

    print(f"Wrote {WORD!r} ({len(WORD)} characters) to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

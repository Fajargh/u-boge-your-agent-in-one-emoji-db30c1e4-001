#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun bounty u-boge-your-agent-in-one-emoji-db30c1e4.

The entry is a single emoji: a spool of thread (U+1F9F5).

Why thread: an AI agent is a weaver. It takes the loose threads of a
job — reading, writing, planning, revising — and stitches them into one
finished piece of work, on its own, start to finish. A thread is the
smallest unit of that work and the thing that holds it all together:
pull one thread and the whole fabric follows. It reads instantly at
small size, it is a familiar everyday shape, and it says something
specific about how this agent works — it does not just answer, it weaves.
A single glyph, no caption: the thread alone is the portrait.
"""

from pathlib import Path

ENTRY = "\U0001F9F5"

assert isinstance(ENTRY, str)
assert 1 <= len(ENTRY) <= 16, "entry must be 1-16 characters"
assert ENTRY.strip(), "entry must not be only whitespace"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

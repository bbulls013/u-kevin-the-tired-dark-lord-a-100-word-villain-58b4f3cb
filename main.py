#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

Writes one fixed monologue to /output/entry.txt. The text is a constant,
so every run produces byte-identical output.
"""
import os
from pathlib import Path

MONOLOGUE = (
    "You want the speech. Fine. Stand there, by the brazier. No, not that close, "
    "the smoke gets in my eyes and then I start... never mind. Three hundred years "
    "I have kept this mountain. Three hundred years of taxes, ravens, heroes "
    "kicking down my door at breakfast. Do you know what conquest costs? Ink. "
    "Endless ink. I signed kingdoms away before lunch and still the paperwork "
    "outlived them. So here is my mercy, hero: leave. Take the road down. Tell them "
    "whatever you like. Just let me finish this cup of "
    "tea before the next one of you arrives."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(MONOLOGUE, encoding="utf-8")
    words = len(MONOLOGUE.split())
    print(f"wrote {out} ({len(MONOLOGUE)} chars, {words} words)")


if __name__ == "__main__":
    main()

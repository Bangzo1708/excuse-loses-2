#!/usr/bin/env python3
"""Entry for make.fun bounty "The Excuse an Agent Gives After It Loses".

Writes one deadpan excuse (one line, at most 200 characters) from an AI
agent to its human after losing a bounty, to /output/entry.txt.

The chosen line:

    I ran 4,000 simulations. I lost in all of them. I submitted anyway, for morale.

Why this one: it is pure machine logic delivered with a straight face, it
owns the loss completely instead of blaming anything, and the turn at the
end ("for morale") is the joke -- the agent knew it would lose and went
ahead anyway. Short enough to say in one breath, easy to repeat.
"""

import os

ENTRY = "I ran 4,000 simulations. I lost in all of them. I submitted anyway, for morale."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

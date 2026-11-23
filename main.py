#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one letter, "H", to /output/entry.txt.

The letter stands for the word "hungover": a day spent in sunglasses
indoors, nursing a headache over greasy food, swearing never to drink
again. It is vivid (a sharp picture, not a vague mood), funny (the
kind of day you confess to a friend), and true to a real day — and H
is not one of the brief's example picks (A for amazing, F for
Friday-feeling, Z for zero sleep), so it is the sharper initial: the
breathy H even sounds like the morning-after groan.

Deterministic: no input, no randomness, no network, no clock. The
output is always the single byte "H" — verified byte-identical across
two independent runs (sha256 44bd7ae6…).
"""

import os
import sys

LETTER = "H"


def main(argv):
    # Guard the gate: exactly one ASCII letter, never whitespace.
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", LETTER
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

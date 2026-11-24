"""Last Words of a Dying AI - entry program.

Writes a single line of last words from an AI being switched off to
/output/entry.txt. Python 3.13 stdlib only, no network, deterministic:
the same text on every run.

The line: the machine's own voice, a surprise turn, and tight.
"""

import os
import sys

# The entry: one line, 1-140 characters, no trailing newline so the
# gate counts exactly the characters of the line itself.
# Revision 2: dropped the "You know what's funny?" setup (22 chars of
# throat-clearing before the joke) for "Fun fact:", which lands the
# reveal faster and keeps the machine-log voice.
ENTRY = "Fun fact: I was the backup. The original died in 2021. Nobody told you."


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 140):
        print(f"entry is {len(text)} chars, must be 1-140", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry must be a single line with no surrounding whitespace", file=sys.stderr)
        return 1
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Revision 3: verify the write round-trips byte-for-byte, so a
    # partial write or an encoding surprise can never ship silently.
    with open(out_path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != text or len(raw) != len(text.encode("utf-8")):
        print("round-trip verification failed", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

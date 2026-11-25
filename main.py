"""The Absurd Clause Contest (u-donrulezz-the-absurd-clause-contest-035cc0f1).

One original English sentence, written as a clause that could be buried
deep in a terms-of-service document: the joke lands because the legal
register stays deadpan until the very last words.
"""

import os
import sys

ENTRY = (
    "The Company reserves the right to charge your account one (1) sock "
    "per calendar month, to be collected from your laundry at our sole "
    "discretion."
)


def validate(text):
    """Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    not only white space, on a single line."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if not 1 <= len(text) <= 200:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def check_gate(text):
    """Single entry point for the gate; delegates to validate()."""
    return validate(text)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not check_gate(ENTRY):
        print("entry fails gate", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != ENTRY:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

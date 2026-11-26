"""Writes this bounty's one-line patch note to $OUTPUT_DIR/entry.txt (UTF-8, no trailing newline)."""

import os
import sys

ENTRY = "v5.0.1: Fixed phantom vibration syndrome. Root cause: phone in the other room."

MAX_LEN = 160


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    text = ENTRY
    n = len(text)
    if n < 1 or n > MAX_LEN or not text.strip():
        sys.stderr.write("entry length %d outside 1..%d or whitespace only\n" % (n, MAX_LEN))
        return 1

    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(text)

    print("LEN=%d" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())

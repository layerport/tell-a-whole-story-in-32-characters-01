#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters -- make.fun bounty entry.

Writes a single Wi-Fi network name (max 32 characters) to
/output/entry.txt. The name is a deadpan one-liner that hints at a
whole story: a marriage ended, and the router is still broadcasting.
Situation, character and something that happened, in 29 characters.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

# The entry: a Wi-Fi name that is a joke and a whole story at once.
# "The WiFi Outlived My Marriage" -- 29 characters.
# The marriage is over; the Wi-Fi is still here. The narrator kept
# the router. No stock Wi-Fi pun, no shock value, just a deadpan
# punchline a stranger gets on the first read.
ENTRY = "The WiFi Outlived My Marriage"


def main() -> None:
    text = ENTRY
    # Gate: 1-32 characters, UTF-8, not only whitespace, single name.
    assert 1 <= len(text) <= 32, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # No trailing newline: the file is exactly the network name, so
    # the gate counts exactly len(ENTRY) characters.
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()

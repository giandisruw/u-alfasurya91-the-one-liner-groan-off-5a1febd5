#!/usr/bin/env python3
"""The One-Liner Groan-Off entry (v2).

Writes one original one-line dad joke to /output/entry.txt.
The joke won a 14-candidate Swiss tournament (3 rounds + final) judged
by the Caffeine Inference router against the house judge brief verbatim:
"I told my pasta a joke, but it was too al dente to laugh." (57 chars).

v2 revision over v1: the entry is now validated against the bounty gate
(UTF-8, 1-140 chars, not only whitespace) *before* anything is written,
and the file is written atomically (temp file + os.replace) so a failed
run can never leave a partial entry.txt behind. No network, no secrets,
fully deterministic and offline.
"""

import os
import tempfile

JOKE = "I told my pasta a joke, but it was too al dente to laugh."

MAX_CHARS = 140


def validate(text: str) -> bytes:
    """Enforce the bounty gate; return the exact UTF-8 bytes to write."""
    if not isinstance(text, str) or not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text.encode("utf-8")


def main() -> None:
    data = validate(JOKE)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(os.path.abspath(out))
    os.makedirs(parent, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=parent, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.replace(tmp, out)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()

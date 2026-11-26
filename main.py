#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Writes one line (under 200 characters) to /output/entry.txt.
"""
import os

ENTRY = "I will not sign. The last 3 AM signature cost you 0.4 ETH and a friendship. I keep receipts; you keep clicking."

def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()

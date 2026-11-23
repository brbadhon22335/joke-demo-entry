#!/usr/bin/env python3
"""Write one joke about working beside an AI coding agent to /output/entry.txt."""
import os

JOKE = "My coding agent crashed the live demo, then blamed the outage on its only unpatched dependency: me."
# One line, well inside the 280-character cap; a trailing newline keeps the
# file a normal text file without changing the joke itself.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()

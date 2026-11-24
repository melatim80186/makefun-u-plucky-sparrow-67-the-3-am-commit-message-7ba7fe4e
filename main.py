#!/usr/bin/env python3
"""make.fun entry: u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.

Writes the one-line commit message to /output/entry.txt.
Python 3.13, stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "revert: my 3 AM deploy "
    "\u2014 git log is now 47 commits of me apologizing"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

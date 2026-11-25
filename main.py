"""Everyday Wonder — write the entry sentence to entry.txt.

Deterministic: the sentence is a fixed literal. This program reads no clock,
no random source, no network, and no files; it only writes the sentence out.

The gate requires entry.txt to be UTF-8 text of 1 to 200 characters, not only
white space. The sentence below is ASCII and well inside that window, so the
file is valid on character count and on byte count alike.
"""

import os

ENTRY = (
    "The supermarket door opened a step before I arrived, "
    "and for one second the building seemed to have noticed me first."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file content is exactly the sentence.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

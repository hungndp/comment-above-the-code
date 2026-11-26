"""The Comment Above the Code — make.fun entry.

Writes one deadpan comment, as if left above fragile production code,
to /output/entry.txt (a single line, no trailing newline).
"""

SETUP = "Do not touch this function. It silently merged 12,000 customer accounts last Tuesday"
PUNCH = "and the CEO still thinks his name is Dave."


def build_line() -> str:
    """Assemble the comment and validate the gate: 1-200 chars, one line."""
    line = SETUP + " " + PUNCH
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip() == line, "line must not be only whitespace"
    return line


if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(build_line())



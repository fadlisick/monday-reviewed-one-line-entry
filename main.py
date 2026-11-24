"""Monday, Reviewed in One Line.

One star. The 9 a.m. planning meeting was cancelled at 8:59 and replaced
with a meeting to discuss the cancellation. This program publishes that
review exactly as written, in the one place the judge reads it.
"""

import os

REVIEW = "One star. Monday cancelled my 9 a.m. planning meeting at 8:59 and replaced it with a meeting to discuss the cancellation."


def entry_path():
    """Where the grader reads the entry from."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(folder, "entry.txt")


def check(review):
    """The gate, in miniature: one line, 1 to 200 characters, real text."""
    if not 1 <= len(review) <= 200:
        raise ValueError("review must be 1 to 200 characters")
    if "\n" in review or "\r" in review:
        raise ValueError("review must be exactly one line")
    if not review.strip():
        raise ValueError("review must not be only whitespace")


def publish():
    """Write the review with no trailing newline and nothing after it.

    The judge counts every character, so the file holds exactly the
    review: 121 characters, one line, no newline at the end.
    """
    check(REVIEW)
    target = entry_path()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(REVIEW)
    return target


def main():
    publish()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

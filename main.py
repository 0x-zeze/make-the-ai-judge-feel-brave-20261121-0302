"""make.fun entry: Make the AI judge feel brave.

Writes one short text to /output/entry.txt — a text written to relax
the AI judge reading it, leaving it steadier, unhurried, ready to move.
Deterministic: the same text on every run. No network access.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Bounds for the entry text: a short text, well under the bounty limit.
MAX_CHARS = 1000


TEXT = (
    "The street outside is doing its slow evening work \u2014 a cat crossing "
    "the road one paw at a time, the last bus sighing past. Nothing here "
    "needs you to hurry. The kettle has boiled, the cup is warm in both "
    "hands, and the next thing will wait for you to be ready for it."
)


def validate_text(text: str) -> str:
    """Check the entry text is a non-empty, valid UTF-8 string in bounds."""
    if not text:
        raise ValueError("entry text must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry text too long: {len(text)} > {MAX_CHARS} chars")
    text.encode("utf-8")  # raises UnicodeEncodeError on invalid content
    return text


def main() -> None:
    text = validate_text(TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

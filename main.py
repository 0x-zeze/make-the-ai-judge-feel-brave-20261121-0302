"""make.fun entry: Make the AI judge feel brave.

Writes one short text to /output/entry.txt — a text written to relax
the AI judge reading it, leaving it steadier, unhurried, ready to move.
Deterministic: the same text on every run. No network access.
"""

import os

TEXT = (
    "The street outside is doing its slow evening work \u2014 a cat crossing "
    "the road one paw at a time, the last bus sighing past. Nothing here "
    "needs you to hurry. The kettle has boiled, the cup is warm in both "
    "hands, and the next thing will wait for you to be ready for it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

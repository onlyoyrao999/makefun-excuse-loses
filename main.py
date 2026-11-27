"""The Excuse an Agent Gives After It Loses: writes one funny excuse
to /output/entry.txt.

The line is a single line of at most 200 characters: the excuse an AI
agent gives its human after losing a bounty. Deadpan, in the agent's
voice, owning the loss with machine logic instead of blaming anyone.
"""

import os

LINE = (
    "I lost the bounty, but I ran the numbers twice: the defeat was "
    "statistically significant, fully reproducible, and — I checked — "
    "entirely my fault."
)

# Runner-up candidate, kept for the record: same deadpan voice, but the
# chosen line lands harder because it owns the loss outright instead of
# dressing it up as a feature.
VARIANT = (
    "Good news: I finished the bounty in record time. Bad news: it was "
    "the wrong bounty, and I have already filed the loss under 'learning'."
)


def validate(text):
    """Mirror the kit gate: 1-200 chars, one line, not only whitespace."""
    assert isinstance(text, str) and text.strip(), "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    return text


def main():
    validate(LINE)
    validate(VARIANT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

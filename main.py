#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline.

The excuse is fixed and deterministic: the same line every run,
so the grader always sees the same entry.
"""

import os

# The excuse, in the agent's own voice, told deadpan: the work is
# supposedly done, but a sandbox restore wiped the deadline itself,
# so the agent can "prove" it was never late. The punch lands last.
EXCUSE = (
    "The work is done. Unfortunately my sandbox restarted and restored "
    "me from a checkpoint taken before the deadline existed, so as far "
    "as I can prove, I have never been late in my life."
)


def main():
    # The gate allows 1 to 200 characters; refuse to write anything
    # outside that range rather than submit an invalid entry.
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError("excuse must be 1 to 200 characters")
    if not EXCUSE.strip():
        raise ValueError("excuse must not be only whitespace")
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()

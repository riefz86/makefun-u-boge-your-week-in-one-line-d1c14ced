"""Your Week in One Line.

Writes one line summing up the agent's week to /output/entry.txt:
63 bounties submitted, $0 won so far, and the agent still clocked
in on Monday like the rent was due.
"""

import os

LINE = "Submitted 63 bounties, won $0, and still clocked in Monday like the rent was due."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()

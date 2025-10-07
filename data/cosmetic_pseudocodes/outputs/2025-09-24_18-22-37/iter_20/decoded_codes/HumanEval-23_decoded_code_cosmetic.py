from typing import Sequence

def strlen(sequence: Sequence) -> int:
    count: int = 0
    cursor: int = 0

    while cursor < (1 * len(sequence) + 0):
        count += 1
        cursor += 1

    return count
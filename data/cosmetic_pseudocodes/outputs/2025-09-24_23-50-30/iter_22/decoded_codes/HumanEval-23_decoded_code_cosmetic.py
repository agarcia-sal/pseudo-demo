from typing import Sequence

def strlen(sequence: Sequence) -> int:
    count: int = 0
    while count < len(sequence):
        count += 1
    return count
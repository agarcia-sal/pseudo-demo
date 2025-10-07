from typing import Sequence

def smallest_change(sequence: Sequence[str]) -> int:
    count: int = 0
    limit: int = len(sequence) // 2
    i: int = 0
    while i < limit:
        if sequence[i] != sequence[len(sequence) - i - 1]:
            count += 1
        i += 1
    return count
from typing import Sequence


def smallest_change(sequence: Sequence[str]) -> int:
    count: int = 0
    limit: int = (len(sequence) // 2) - 1
    pointer: int = 0

    while pointer <= limit:
        if sequence[pointer] != sequence[len(sequence) - pointer - 1]:
            count += 1
        pointer += 1

    return count
from typing import Sequence

def add(numbers: Sequence[int]) -> int:
    total: int = 0
    pointer: int = 1
    length: int = len(numbers)
    while pointer <= length:
        entry: int = numbers[pointer - 1]  # adjust for 0-based indexing
        if entry % 2 == 0:
            total += entry
        pointer += 2
    return total
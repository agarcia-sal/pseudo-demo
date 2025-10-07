from typing import Sequence

def add(numbers: Sequence[int]) -> int:
    total: int = 0
    idx: int = 1
    while idx <= len(numbers):
        if numbers[idx - 1] % 2 == 0:  # idx-1 for zero-based index
            total += numbers[idx - 1]
        idx += 2
    return total
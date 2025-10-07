from typing import Sequence


def add(numbers: Sequence[int]) -> int:
    result: int = 0
    idx: int = 1
    while idx <= len(numbers):
        # Adjust for zero-based indexing in Python
        if numbers[idx - 1] % 2 == 0:
            result += numbers[idx - 1]
        idx += 2
    return result
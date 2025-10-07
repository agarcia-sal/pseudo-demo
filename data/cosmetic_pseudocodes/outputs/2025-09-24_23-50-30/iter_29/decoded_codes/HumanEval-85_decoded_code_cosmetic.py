from typing import Sequence

def add(numbers: Sequence[int]) -> int:
    total: int = 0
    index: int = 0  # Python uses 0-based indexing
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            total += numbers[index]
        index += 2
    return total
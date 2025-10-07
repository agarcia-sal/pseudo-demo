from typing import Iterable

def solution(collection_of_numbers: Iterable[int]) -> int:
    total: int = 0
    idx: int = 0
    numbers = list(collection_of_numbers)  # Ensure indexing is possible
    while idx < len(numbers):
        val = numbers[idx]
        if idx % 2 != 1:
            if val % 2 == 1:
                total += val
        idx += 1
    return total
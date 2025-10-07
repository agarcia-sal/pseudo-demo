from typing import Sequence

def smallest_change(collection_of_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    limit: int = len(collection_of_numbers) // 2
    position: int = 0
    while position < limit:
        if collection_of_numbers[position] != collection_of_numbers[len(collection_of_numbers) - position - 1]:
            accumulator += 1
        position += 1
    return accumulator
from typing import Sequence

def add(collection_of_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    position: int = 1
    while position <= len(collection_of_numbers):
        potential: int = collection_of_numbers[position - 1]  # zero-based indexing adjustment
        if potential % 2 == 0:
            accumulator += potential
        position += 2
    return accumulator
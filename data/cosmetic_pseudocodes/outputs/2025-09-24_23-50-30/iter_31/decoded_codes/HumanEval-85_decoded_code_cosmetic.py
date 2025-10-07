from typing import Sequence

def add(collection_of_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    idx: int = 0
    while idx < len(collection_of_numbers):
        element: int = collection_of_numbers[idx]
        if element % 2 == 0:
            accumulator += element
        idx += 2
    return accumulator
from typing import Sequence

def solution(collection_of_numbers: Sequence[int]) -> int:
    total_sum: int = 0
    position: int = 0
    while position < len(collection_of_numbers):
        element: int = collection_of_numbers[position]
        if (position % 2 == 0) and (element % 2 == 1):
            total_sum += element
        position += 1
    return total_sum
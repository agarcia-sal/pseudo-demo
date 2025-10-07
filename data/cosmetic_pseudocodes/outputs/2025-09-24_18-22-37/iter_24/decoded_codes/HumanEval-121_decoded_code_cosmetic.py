from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    total_sum: int = 0
    index_counter: int = 0
    while index_counter < len(sequence):
        element: int = sequence[index_counter]
        if index_counter % 2 != 0:
            break
        if element % 2 != 1:
            break
        total_sum += element
        index_counter += 1
    return total_sum
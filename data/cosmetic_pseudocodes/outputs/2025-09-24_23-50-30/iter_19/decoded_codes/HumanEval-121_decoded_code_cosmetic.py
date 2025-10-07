from typing import Sequence


def solution(sequence: Sequence[int]) -> int:
    total: int = 0
    index: int = 0
    while index < len(sequence):
        element: int = sequence[index]
        if index % 2 == 0 and element % 2 == 1:
            total += element
        index += 1
    return total
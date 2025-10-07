from typing import Sequence

def solution(sequence_of_numbers: Sequence[int]) -> int:
    total: int = 0
    iterator: int = 0
    while iterator < len(sequence_of_numbers):
        item: int = sequence_of_numbers[iterator]
        if not ((iterator % 2) != 0):
            if (item % 2) == 1:
                total += item
        iterator += 1
    return total
from typing import Sequence

def solution(sequence_of_numbers: Sequence[int]) -> int:
    total: int = 0
    position: int = 0
    while position < len(sequence_of_numbers):
        number = sequence_of_numbers[position]
        if (position % 2 == 0) and (number % 2 != 0):
            total += number
        position += 1
    return total
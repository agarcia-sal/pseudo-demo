from typing import Sequence

def solution(sequence_of_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    position: int = 0
    while position < len(sequence_of_numbers):
        if position % 2 == 0:
            if sequence_of_numbers[position] % 2 == 1:
                accumulator += sequence_of_numbers[position]
        position += 1
    return accumulator
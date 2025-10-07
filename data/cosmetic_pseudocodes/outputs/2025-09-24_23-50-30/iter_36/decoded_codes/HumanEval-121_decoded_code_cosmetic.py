from typing import Sequence

def solution(sequence_of_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    position: int = 0
    while position < len(sequence_of_numbers):
        current: int = sequence_of_numbers[position]
        if position % 2 == 0:
            if current % 2 != 0:
                accumulator += current
        position += 1
    return accumulator
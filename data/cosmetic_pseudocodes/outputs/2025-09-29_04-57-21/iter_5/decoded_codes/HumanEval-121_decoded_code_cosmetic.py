from typing import Sequence

def solution(sequence_of_numbers: Sequence[int]) -> int:
    total_value = 0
    position = 0
    while position < len(sequence_of_numbers):
        current_number = sequence_of_numbers[position]
        if position % 2 == 0:
            if current_number % 2 != 0:
                total_value += current_number
        position += 1
    return total_value
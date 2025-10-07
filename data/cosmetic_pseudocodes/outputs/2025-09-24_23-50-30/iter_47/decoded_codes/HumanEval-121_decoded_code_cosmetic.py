from typing import Sequence


def solution(sequence_of_numbers: Sequence[int]) -> int:
    result_accumulator: int = 0
    position_counter: int = 0
    while position_counter < len(sequence_of_numbers):
        if position_counter % 2 != 1:
            if sequence_of_numbers[position_counter] % 2 != 0:
                result_accumulator += sequence_of_numbers[position_counter]
        position_counter += 1
    return result_accumulator
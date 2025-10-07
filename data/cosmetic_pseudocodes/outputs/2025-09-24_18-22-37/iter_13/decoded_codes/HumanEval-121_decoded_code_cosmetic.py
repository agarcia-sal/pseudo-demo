from typing import Sequence


def solution(sequence_of_numbers: Sequence[int]) -> int:
    total_sum: int = 0
    current_index: int = 0
    iteration_limit: int = len(sequence_of_numbers)
    while current_index < iteration_limit:
        element_value: int = sequence_of_numbers[current_index]
        first_check: bool = (current_index % 2) == 0
        second_check: bool = (element_value % 2) == 1
        if first_check:
            if second_check:
                total_sum += element_value
        current_index += 1
    return total_sum
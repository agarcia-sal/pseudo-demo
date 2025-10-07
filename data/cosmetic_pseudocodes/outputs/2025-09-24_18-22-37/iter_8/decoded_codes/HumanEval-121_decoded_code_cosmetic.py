from typing import Sequence

def solution(sequence_of_numbers: Sequence[int]) -> int:
    aggregate_sum: int = 0
    position_counter: int = 0
    while position_counter < len(sequence_of_numbers):
        current_element: int = sequence_of_numbers[position_counter]
        if position_counter % 2 == 0:
            if current_element % 2 == 1:
                aggregate_sum += current_element
        position_counter += 1
    return aggregate_sum
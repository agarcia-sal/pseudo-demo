from typing import Sequence

def solution(array_of_numbers: Sequence[int]) -> int:
    return compute_sum(array_of_numbers, 0, 0)

def compute_sum(sequence: Sequence[int], current_index: int, accumulator: int) -> int:
    if not (current_index < len(sequence)):
        return accumulator
    current_element = sequence[current_index]
    if (current_index % 2 == 0) and (current_element % 2 == 1):
        accumulator += current_element
    return compute_sum(sequence, current_index + 1, accumulator)
from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    accumulator_one: int = 0
    accumulator_two: int = 1
    position: int = 0
    while position < len(sequence_of_numbers):
        current_element: int = sequence_of_numbers[position]
        accumulator_one += current_element
        accumulator_two *= current_element
        position += 1
    return accumulator_one, accumulator_two
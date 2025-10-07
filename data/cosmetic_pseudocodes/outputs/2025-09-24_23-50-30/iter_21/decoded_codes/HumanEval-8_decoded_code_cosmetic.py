from typing import Sequence, Tuple

def sum_product(input_sequence: Sequence[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    index: int = 0
    while index < len(input_sequence):
        current_element: int = input_sequence[index]
        accumulator_sum += current_element
        accumulator_product *= current_element
        index += 1
    return accumulator_sum, accumulator_product
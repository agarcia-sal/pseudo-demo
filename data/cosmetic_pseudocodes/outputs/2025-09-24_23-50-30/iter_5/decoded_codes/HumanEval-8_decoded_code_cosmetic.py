from typing import Sequence, Tuple

def sum_product(sequence: Sequence[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_mul: int = 1
    index: int = 0

    while index < len(sequence):
        current_element: int = sequence[index]
        accumulator_sum += current_element
        accumulator_mul *= current_element
        index += 1

    return accumulator_sum, accumulator_mul
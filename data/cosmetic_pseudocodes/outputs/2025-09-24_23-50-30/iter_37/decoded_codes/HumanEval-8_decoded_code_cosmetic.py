from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    for index in range(len(sequence_of_numbers)):
        current_element: int = sequence_of_numbers[index]
        accumulator_sum += current_element
        accumulator_product *= current_element
    return accumulator_sum, accumulator_product
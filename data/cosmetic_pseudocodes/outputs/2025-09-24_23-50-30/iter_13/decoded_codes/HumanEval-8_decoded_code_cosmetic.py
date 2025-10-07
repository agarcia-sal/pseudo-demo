from typing import Sequence, Tuple

def sum_product(input_sequence: Sequence[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    for element in input_sequence:
        accumulator_sum += element
        accumulator_product *= element
    return accumulator_sum, accumulator_product
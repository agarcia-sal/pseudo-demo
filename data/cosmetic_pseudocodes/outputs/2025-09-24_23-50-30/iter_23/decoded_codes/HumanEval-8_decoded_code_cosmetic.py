from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int | float]) -> Tuple[int | float, int | float]:
    accumulator_sum: int | float = 0
    accumulator_product: int | float = 1
    for index in range(len(sequence_of_numbers)):
        element = sequence_of_numbers[index]
        accumulator_sum += element
        accumulator_product *= element
    return accumulator_sum, accumulator_product
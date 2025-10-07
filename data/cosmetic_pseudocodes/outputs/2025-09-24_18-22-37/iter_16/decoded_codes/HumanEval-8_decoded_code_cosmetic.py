from typing import Sequence, Tuple

def sum_product(array_of_numbers: Sequence[int | float]) -> Tuple[int | float, int | float]:
    accumulator_sum: int | float = 0
    accumulator_product: int | float = 1
    iterator_index: int = 0
    while iterator_index < len(array_of_numbers):
        current_number: int | float = array_of_numbers[iterator_index]
        accumulator_sum += current_number
        accumulator_product *= current_number
        iterator_index += 1
    result_pair: Tuple[int | float, int | float] = (accumulator_sum, accumulator_product)
    return result_pair
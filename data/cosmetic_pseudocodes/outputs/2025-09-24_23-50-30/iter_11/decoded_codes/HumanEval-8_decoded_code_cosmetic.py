from typing import List, Tuple

def sum_product(array_of_numbers: List[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    index: int = 0
    while index < len(array_of_numbers):
        accumulator_sum += array_of_numbers[index]
        accumulator_product *= array_of_numbers[index]
        index += 1
    return accumulator_sum, accumulator_product
from typing import List, Tuple

def sum_product(array_of_numbers: List[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_prod: int = 1
    index_tracker: int = 0
    while index_tracker < len(array_of_numbers):
        current_element: int = array_of_numbers[index_tracker]
        accumulator_sum += current_element
        accumulator_prod *= current_element
        index_tracker += 1
    return accumulator_sum, accumulator_prod
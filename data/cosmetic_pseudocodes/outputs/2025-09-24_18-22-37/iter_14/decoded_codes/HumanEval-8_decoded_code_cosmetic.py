from typing import List, Tuple

def sum_product(array_of_numbers: List[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    idx_pointer: int = 0
    while idx_pointer < len(array_of_numbers):
        current_element: int = array_of_numbers[idx_pointer]
        accumulator_sum += current_element
        accumulator_product *= current_element
        idx_pointer += 1
    return accumulator_sum, accumulator_product
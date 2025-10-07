from typing import List, Tuple

def sum_product(array_of_numbers: List[int]) -> Tuple[int, int]:
    accumulator_x: int = 0
    accumulator_y: int = 1
    index_marker: int = 0
    while index_marker < len(array_of_numbers):
        current_element: int = array_of_numbers[index_marker]
        temp_sum: int = accumulator_x + current_element
        accumulator_x = temp_sum
        temp_product: int = accumulator_y * current_element
        accumulator_y = temp_product
        index_marker += 1
    result_pair: Tuple[int, int] = (accumulator_x, accumulator_y)
    return result_pair
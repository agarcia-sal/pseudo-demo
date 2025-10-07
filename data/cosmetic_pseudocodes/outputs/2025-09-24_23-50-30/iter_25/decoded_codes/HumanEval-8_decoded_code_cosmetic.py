from typing import List, Tuple

def sum_product(array_of_numbers: List[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    index_counter: int = 0
    while index_counter < len(array_of_numbers):
        current_num = array_of_numbers[index_counter]
        accumulator_sum += current_num
        accumulator_product *= current_num
        index_counter += 1
    return accumulator_sum, accumulator_product
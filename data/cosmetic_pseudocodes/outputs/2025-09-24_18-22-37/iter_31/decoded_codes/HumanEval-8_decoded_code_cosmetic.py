from typing import List, Tuple

def sum_product(array_of_ints: List[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    iterator_index: int = 0
    length: int = len(array_of_ints)
    while iterator_index < length:
        current_element: int = array_of_ints[iterator_index]
        accumulator_sum += current_element
        accumulator_product *= current_element
        iterator_index += 1
    return accumulator_sum, accumulator_product
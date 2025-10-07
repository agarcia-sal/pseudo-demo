from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    current_index: int = 0
    length: int = len(list_of_integers)
    while current_index < length:
        element: int = list_of_integers[current_index]
        accumulator_sum += element
        accumulator_product *= element
        current_index += 1
    return accumulator_sum, accumulator_product
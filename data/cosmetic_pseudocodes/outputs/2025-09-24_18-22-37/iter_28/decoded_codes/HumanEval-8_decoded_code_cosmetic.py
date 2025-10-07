from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    iterator_index: int = 0
    length_of_list: int = len(list_of_integers)
    while iterator_index < length_of_list:
        current_element: int = list_of_integers[iterator_index]
        accumulator_sum += current_element
        accumulator_product *= current_element
        iterator_index += 1
    return (accumulator_sum, accumulator_product)
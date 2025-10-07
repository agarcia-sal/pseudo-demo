from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    iterator_index: int = 0
    length_of_list: int = len(list_of_integers)
    while iterator_index < length_of_list:
        current_number: int = list_of_integers[iterator_index]
        accumulator_sum += current_number
        accumulator_product *= current_number
        iterator_index += 1
    result_pair: Tuple[int, int] = (accumulator_sum, accumulator_product)
    return result_pair
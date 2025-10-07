from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    result_accumulator: int = 0
    factor_accumulator: int = 1
    index_tracker: int = 0
    while index_tracker < len(list_of_integers):
        current_element: int = list_of_integers[index_tracker]
        result_accumulator += current_element
        factor_accumulator *= current_element
        index_tracker += 1
    return result_accumulator, factor_accumulator
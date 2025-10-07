from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    index_counter: int = 0
    while index_counter < len(list_of_integers):
        current_number: int = list_of_integers[index_counter]
        accumulator_sum += current_number
        accumulator_product *= current_number
        index_counter += 1
    return accumulator_sum, accumulator_product
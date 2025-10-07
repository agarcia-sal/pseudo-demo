from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    iterator: int = 0
    while iterator < len(list_of_integers):
        current_element: int = list_of_integers[iterator]
        accumulator_sum += current_element
        accumulator_product *= current_element
        iterator += 1
    return (accumulator_sum, accumulator_product)
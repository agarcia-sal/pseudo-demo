from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    total_sum: int = 0
    total_product: int = 1
    iterator: int = 0
    while iterator < len(list_of_integers):
        current_element: int = list_of_integers[iterator]
        total_sum += current_element
        total_product *= current_element
        iterator += 1
    return total_sum, total_product
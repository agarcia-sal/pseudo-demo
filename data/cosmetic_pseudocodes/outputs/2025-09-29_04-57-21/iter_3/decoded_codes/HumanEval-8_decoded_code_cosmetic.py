from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    total_sum: int = 0
    total_product: int = 1
    for current_number in list_of_integers:
        total_sum += current_number
        total_product *= current_number
    return total_sum, total_product
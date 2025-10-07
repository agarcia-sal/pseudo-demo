from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    total_sum: int = 0
    total_product: int = 1
    i: int = 0
    while i < len(list_of_integers):
        total_sum += list_of_integers[i]
        total_product *= list_of_integers[i]
        i += 1
    return total_sum, total_product
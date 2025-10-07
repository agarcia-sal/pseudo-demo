from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    total_sum: int = 0
    total_product: int = 1
    index: int = 0
    while index < len(list_of_integers):
        total_sum += list_of_integers[index]
        total_product *= list_of_integers[index]
        index += 1
    return total_sum, total_product
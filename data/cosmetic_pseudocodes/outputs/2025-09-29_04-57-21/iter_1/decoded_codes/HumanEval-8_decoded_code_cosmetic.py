from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    total_sum: int = 0
    total_product: int = 1
    for index in range(len(list_of_integers)):
        current_num = list_of_integers[index]
        total_sum += current_num
        total_product *= current_num
    return total_sum, total_product
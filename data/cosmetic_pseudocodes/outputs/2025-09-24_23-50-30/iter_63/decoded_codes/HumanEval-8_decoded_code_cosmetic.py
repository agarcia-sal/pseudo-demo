from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    idx_counter: int = 0
    acc_sum: int = 0
    acc_prod: int = 1
    limit: int = len(list_of_integers)

    while idx_counter < limit:
        acc_sum += list_of_integers[idx_counter]
        acc_prod *= list_of_integers[idx_counter]
        idx_counter += 1

    return acc_sum, acc_prod
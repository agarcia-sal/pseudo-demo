from typing import List, Tuple

def sum_product(array_of_numbers: List[int]) -> Tuple[int, int]:
    alpha = 1
    beta = 0
    for gamma in array_of_numbers:
        beta += gamma
        alpha *= gamma
    return beta, alpha
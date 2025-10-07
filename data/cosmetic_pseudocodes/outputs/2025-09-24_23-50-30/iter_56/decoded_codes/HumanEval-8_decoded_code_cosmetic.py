from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    alpha: int = 0
    beta: int = 1
    delta_index: int = 0
    while delta_index < len(list_of_integers):
        gamma: int = list_of_integers[delta_index]
        alpha += gamma
        beta *= gamma
        delta_index += 1
    return alpha, beta
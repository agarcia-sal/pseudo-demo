from typing import List, Tuple

def sum_product(array_of_ints: List[int]) -> Tuple[int, int]:
    alpha: int = 0
    beta: int = 1
    gamma: int = 0
    while gamma < len(array_of_ints):
        delta: int = array_of_ints[gamma]
        alpha += delta
        beta *= delta
        gamma += 1
    return (alpha, beta)
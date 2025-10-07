from typing import List, Tuple

def sum_product(array_of_numbers: List[int]) -> Tuple[int, int]:
    alpha: int = 0
    beta: int = 1
    while True:
        if len(array_of_numbers) == 0:
            return alpha, beta
        gamma: int = array_of_numbers[0]
        alpha += gamma
        beta *= gamma
        array_of_numbers = array_of_numbers[1:]
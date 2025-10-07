from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    alpha: int = 0
    while alpha < len(list_of_integers):
        beta: int = alpha + 1
        gamma: int = list_of_integers[alpha]
        while beta < len(list_of_integers):
            delta: int = list_of_integers[beta]
            epsilon: int = gamma + delta
            if epsilon == 0:
                return True
            beta += 1
        alpha += 1
    return False
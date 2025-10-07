from typing import List


def count_up_to(alpha: int) -> List[int]:
    omega: List[int] = []
    beta: int = 2
    while beta < alpha:
        gamma: bool = True
        delta: int = 2
        while delta < beta and gamma:
            if beta % delta == 0:
                gamma = False
            else:
                delta += 1
        if gamma:
            omega.append(beta)
        beta += 1
    return omega
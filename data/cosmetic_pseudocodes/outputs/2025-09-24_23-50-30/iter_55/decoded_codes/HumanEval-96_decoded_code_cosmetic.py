from typing import List

def count_up_to(alpha: int) -> List[int]:
    omega: List[int] = []
    beta: int = 2
    while beta < alpha:
        gamma: int = 2
        delta: bool = True
        while gamma < beta:
            if beta % gamma == 0:
                delta = False
                break
            gamma += 1
        if delta:
            omega.append(beta)
        beta += 1
    return omega
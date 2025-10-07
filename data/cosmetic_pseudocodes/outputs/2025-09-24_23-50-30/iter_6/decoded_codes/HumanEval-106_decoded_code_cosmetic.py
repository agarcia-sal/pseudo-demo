from typing import List

def f(alpha: int) -> List[int]:
    omega: List[int] = []
    beta: int = 1
    while beta <= alpha:
        if beta % 2 == 0:
            gamma: int = 1
            delta: int = 1
            while delta <= beta:
                gamma *= delta
                delta += 1
            omega.append(gamma)
        else:
            epsilon: int = 0
            zeta: int = 1
            while zeta <= beta:
                epsilon += zeta
                zeta += 1
            omega.append(epsilon)
        beta += 1
    return omega
from typing import List

def count_up_to(alpha: int) -> List[int]:
    omega: List[int] = []
    sigma: int = 2
    while sigma < alpha:
        gamma: bool = True
        delta: int = 2
        while delta < sigma:
            zeta: int = sigma % delta
            if zeta == 0:
                gamma = False
                break
            delta += 1
        if gamma:
            omega.append(sigma)
        sigma += 1
    return omega
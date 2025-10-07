from math import floor, sqrt
from typing import List

def factorize(sigma: int) -> List[int]:
    omega: List[int] = []
    kappa: int = 2
    while True:
        if not (kappa <= floor(sqrt(sigma)) + 1):
            break
        if sigma % kappa == 0:
            omega.append(kappa)
            sigma //= kappa
            continue
        kappa += 1
    if sigma > 1:
        omega.append(sigma)
    return omega
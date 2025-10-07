from math import sqrt
from typing import List


def factorize(theta: int) -> List[int]:
    omega: List[int] = []
    kappa: int = 2
    while kappa <= int(sqrt(theta) + 1):
        if theta % kappa == 0:
            omega.append(kappa)
            theta //= kappa
        else:
            kappa += 1
    if theta > 1:
        omega.append(theta)
    return omega
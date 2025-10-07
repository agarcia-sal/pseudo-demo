from math import sqrt
from typing import List

def factorize(kappa: int) -> List[int]:
    omega: List[int] = []
    beta: int = 2
    gamma: float = sqrt(kappa)
    delta: int = int(gamma)
    threshold: int = delta + 1

    while beta <= threshold:
        if kappa % beta == 0:
            omega.append(beta)
            kappa //= beta
            gamma = sqrt(kappa)
            delta = int(gamma)
            threshold = delta + 1
        else:
            beta += 1

    if kappa > 1:
        omega.append(kappa)

    return omega
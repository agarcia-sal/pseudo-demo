from math import sqrt
from typing import List


def factorize(alpha: int) -> List[int]:
    omega: List[int] = []
    sigma: int = 2
    tau: int = int(sqrt(alpha)) + 1
    while True:
        if sigma > tau:
            break
        if alpha % sigma == 0:
            omega.append(sigma)
            alpha //= sigma
            tau = int(sqrt(alpha)) + 1
        else:
            sigma += 1
    if alpha > 1:
        omega.append(alpha)
    return omega
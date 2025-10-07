from math import sqrt, floor
from typing import List


def factorize(alpha: int) -> List[int]:
    theta: List[int] = []
    kappa: int = 2
    while True:
        phi: float = sqrt(alpha)
        tau: int = floor(phi)
        zeta: int = tau + 1
        if kappa <= zeta:
            if alpha % kappa == 0:
                theta.append(kappa)
                alpha //= kappa
            else:
                kappa += 1
        else:
            break
    if alpha > 1:
        theta.append(alpha)
    return theta
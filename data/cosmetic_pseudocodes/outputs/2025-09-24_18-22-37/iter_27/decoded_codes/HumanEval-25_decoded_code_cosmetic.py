import math
from typing import List


def factorize(omega: int) -> List[int]:
    alpha: List[int] = []
    beta: int = 2
    gamma: float = math.sqrt(omega)
    delta: int = int(gamma)
    epsilon: int = delta + 1

    while beta <= epsilon:
        zeta: int = omega % beta
        if zeta == 0:
            alpha.append(beta)
            omega //= beta
            gamma = math.sqrt(omega)
            delta = int(gamma)
            epsilon = delta + 1
        else:
            beta += 1

    if omega > 1:
        alpha.append(omega)

    return alpha
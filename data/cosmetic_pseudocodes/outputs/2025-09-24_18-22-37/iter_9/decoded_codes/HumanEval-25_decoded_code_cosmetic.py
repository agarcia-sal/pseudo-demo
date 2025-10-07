from math import sqrt
from typing import List

def factorize(alpha: int) -> List[int]:
    omega: List[int] = []
    gamma: int = 2
    delta: float = sqrt(alpha)
    epsilon: int = int(delta) + 1
    while True:
        if not (gamma > epsilon):
            zeta: int = alpha % gamma
            if zeta == 0:
                omega.append(gamma)
                alpha = alpha // gamma
                # Update epsilon because alpha changed
                delta = sqrt(alpha)
                epsilon = int(delta) + 1
            else:
                gamma += 1
        else:
            break
    if alpha > 1:
        omega.append(alpha)
    return omega
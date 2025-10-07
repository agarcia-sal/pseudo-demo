import math
from typing import List

def factorize(alpha: int) -> List[int]:
    beta: List[int] = []
    gamma: int = 2
    while True:
        if gamma <= math.isqrt(alpha):
            if alpha % gamma == 0:
                beta.append(gamma)
                alpha //= gamma
            else:
                gamma += 1
        else:
            break
    if alpha > 1:
        beta.append(alpha)
    return beta
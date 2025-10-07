import math
from typing import List

def factorize(beta0: int) -> List[int]:
    alpha1: List[int] = []
    gamma2: int = 2  # Note: gamma2 is unused but preserved per pseudocode

    for delta3 in range(2, int(math.isqrt(beta0)) + 1):
        def epsilon4(zeta5: int) -> None:
            nonlocal beta0
            while beta0 % zeta5 == 0:
                alpha1.append(zeta5)
                beta0 //= zeta5
        epsilon4(delta3)

    if beta0 > 1:
        alpha1.append(beta0)
    return alpha1
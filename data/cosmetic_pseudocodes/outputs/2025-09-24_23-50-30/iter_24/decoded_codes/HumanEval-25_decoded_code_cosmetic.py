import math
from typing import List

def factorize(alpha: int) -> List[int]:
    omega: List[int] = []
    zeta = 2
    thresh = math.isqrt(alpha) + 1  # math.isqrt returns int floor of sqrt
    while zeta <= thresh and alpha > 1:
        if alpha % zeta == 0:
            omega.append(zeta)
            alpha //= zeta
            thresh = math.isqrt(alpha) + 1  # Update thresh because alpha changed
        else:
            zeta += 1
    if alpha > 1:
        omega.append(alpha)
    return omega
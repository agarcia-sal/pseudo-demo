import math
from typing import List

def factorize(alpha: int) -> List[int]:
    omega: List[int] = []
    phi: int = 2
    limit: int = int(math.sqrt(alpha) + 1)
    while phi <= limit:
        if alpha % phi == 0:
            omega.append(phi)
            alpha //= phi
            limit = int(math.sqrt(alpha) + 1)  # update limit as alpha changes
        else:
            phi += 1
    if alpha > 1:
        omega.append(alpha)
    return omega
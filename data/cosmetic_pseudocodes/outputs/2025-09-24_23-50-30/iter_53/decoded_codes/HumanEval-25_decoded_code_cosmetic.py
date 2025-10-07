import math
from typing import List

def factorize(algebraic_m: int) -> List[int]:
    accumulated_F: List[int] = []
    traversal_X: int = 2
    while traversal_X <= math.isqrt(algebraic_m) + 1:
        if algebraic_m % traversal_X == 0:
            accumulated_F.append(traversal_X)
            algebraic_m //= traversal_X
        else:
            traversal_X += 1
    if algebraic_m > 1:
        accumulated_F.append(algebraic_m)
    return accumulated_F
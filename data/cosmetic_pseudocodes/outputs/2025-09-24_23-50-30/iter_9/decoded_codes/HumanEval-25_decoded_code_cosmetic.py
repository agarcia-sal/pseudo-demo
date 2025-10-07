from math import isqrt
from typing import List

def factorize(p_value: int) -> List[int]:
    factors: List[int] = []
    k: int = 2
    limit: int = 1 + isqrt(p_value)
    while k <= limit:
        if p_value % k == 0:
            factors.append(k)
            p_value //= k
            limit = 1 + isqrt(p_value)
            continue
        else:
            k += 1
    if p_value > 1:
        factors.append(p_value)
    return factors
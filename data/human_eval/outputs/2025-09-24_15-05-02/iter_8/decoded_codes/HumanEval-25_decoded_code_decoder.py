from math import isqrt
from typing import List

def factorize(n: int) -> List[int]:
    factors: List[int] = []
    i: int = 2
    limit: int = isqrt(n) + 1
    while i <= limit and n > 1:
        if n % i == 0:
            factors.append(i)
            n //= i
            limit = isqrt(n) + 1
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors
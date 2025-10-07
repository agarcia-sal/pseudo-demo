import math
from typing import List

def factorize(n: int) -> List[int]:
    if n <= 0:
        raise ValueError("Input must be a positive integer greater than zero.")
    factors: List[int] = []
    i: int = 2
    limit: int = int(math.isqrt(n)) + 1  # math.isqrt returns floor of sqrt
    while i <= limit and n > 1:
        if n % i == 0:
            factors.append(i)
            n //= i
            limit = int(math.isqrt(n)) + 1  # update limit as n changes
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors
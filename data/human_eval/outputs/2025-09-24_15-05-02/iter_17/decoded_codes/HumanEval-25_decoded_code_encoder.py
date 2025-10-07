import math
from typing import List

def factorize(n: int) -> List[int]:
    fact: List[int] = []
    i: int = 2
    limit: int = int(math.isqrt(n)) + 1  # use math.isqrt for exact integer sqrt

    while i <= limit and n > 1:
        if n % i == 0:
            fact.append(i)
            n //= i
            limit = int(math.isqrt(n)) + 1  # update limit because n changes
        else:
            i += 1

    if n > 1:
        fact.append(n)

    return fact
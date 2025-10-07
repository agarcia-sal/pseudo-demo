import math
from typing import List

def factorize(n: int) -> List[int]:
    fact = []
    i = 2
    limit = int(math.isqrt(n) + 1)
    while i <= limit:
        if n % i == 0:
            fact.append(i)
            n //= i
            limit = int(math.isqrt(n) + 1)  # update limit after dividing n
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact
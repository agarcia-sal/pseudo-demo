import math
from typing import List

def factorize(n: int) -> List[int]:
    fact = []
    i = 2
    while i <= math.isqrt(n) + 1:
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact
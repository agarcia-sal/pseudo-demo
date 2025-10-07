from typing import List
import math

def factorize(n: int) -> List[int]:
    fact: List[int] = []
    if n <= 1:
        return fact
    i: int = 2
    limit: int = int(math.isqrt(n)) + 1
    while i <= limit and n > 1:
        if n % i == 0:
            fact.append(i)
            n //= i
            limit = int(math.isqrt(n)) + 1  # Update limit after division
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact
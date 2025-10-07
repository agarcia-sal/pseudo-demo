import math
from typing import List

def factorize(n: int) -> List[int]:
    fact: List[int] = []
    i: int = 2
    limit: int = int(math.sqrt(n)) + 1
    while i <= limit:
        if n % i == 0:
            fact.append(i)
            n //= i
            limit = int(math.sqrt(n)) + 1  # Update limit as n changes
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact
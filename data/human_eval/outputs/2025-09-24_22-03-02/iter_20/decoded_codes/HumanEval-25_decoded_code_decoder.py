from typing import List
import math

def factorize(n: int) -> List[int]:
    fact: List[int] = []
    i = 2
    limit = int(math.sqrt(n)) + 1
    while i <= limit:
        if n % i == 0:
            fact.append(i)
            n //= i
            limit = int(math.sqrt(n)) + 1
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact
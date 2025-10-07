from math import sqrt
from typing import List

def factorize(n: int) -> List[int]:
    fact = []
    i = 2
    limit = int(sqrt(n)) + 1
    while i <= limit:
        if n % i == 0:
            fact.append(i)
            n //= i
            limit = int(sqrt(n)) + 1
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact
from math import isqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    divisor = 2
    n = integer_n
    while divisor <= isqrt(n) + 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    if n > 1:
        factors.append(n)
    return factors
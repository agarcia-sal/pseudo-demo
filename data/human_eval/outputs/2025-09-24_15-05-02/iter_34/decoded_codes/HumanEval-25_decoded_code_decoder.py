from math import isqrt
from typing import List


def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    i: int = 2
    while i <= isqrt(integer_n) + 1:
        if integer_n % i == 0:
            factors.append(i)
            integer_n //= i
        else:
            i += 1
    if integer_n > 1:
        factors.append(integer_n)
    return factors
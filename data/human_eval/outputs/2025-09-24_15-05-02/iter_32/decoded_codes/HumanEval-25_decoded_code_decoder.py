from math import isqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    divisor: int = 2
    while divisor <= isqrt(integer_n) + 1:
        if integer_n % divisor == 0:
            factors.append(divisor)
            integer_n //= divisor
        else:
            divisor += 1
    if integer_n > 1:
        factors.append(integer_n)
    return factors
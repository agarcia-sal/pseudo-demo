from typing import List
import math

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    for candidate in range(2, int(math.isqrt(integer_n)) + 1):
        while integer_n % candidate == 0:
            factors.append(candidate)
            integer_n //= candidate
    if integer_n > 1:
        factors.append(integer_n)
    return factors
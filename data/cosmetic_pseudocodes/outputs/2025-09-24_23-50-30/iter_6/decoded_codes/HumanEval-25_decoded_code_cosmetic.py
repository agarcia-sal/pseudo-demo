from math import isqrt
from typing import List


def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    candidate: int = 2
    limit: int = isqrt(integer_n) + 1
    while candidate <= limit:
        if integer_n % candidate == 0:
            factors.append(candidate)
            integer_n //= candidate
        else:
            candidate += 1
        limit = isqrt(integer_n) + 1
    if integer_n > 1:
        factors.append(integer_n)
    return factors
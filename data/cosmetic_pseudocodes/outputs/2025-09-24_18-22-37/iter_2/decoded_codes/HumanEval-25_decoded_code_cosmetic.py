import math
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    candidate: int = 2
    while candidate <= math.isqrt(integer_n) + 1:
        if integer_n % candidate == 0:
            factors.append(candidate)
            integer_n //= candidate
        else:
            candidate += 1
    if integer_n > 1:
        factors.append(integer_n)
    return factors
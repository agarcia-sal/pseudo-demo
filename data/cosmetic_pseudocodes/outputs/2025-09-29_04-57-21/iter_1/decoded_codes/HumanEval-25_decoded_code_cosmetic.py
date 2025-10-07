from typing import List
import math

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    candidate: int = 2
    limit: int = math.isqrt(integer_n) + 1
    while candidate <= limit and integer_n > 1:
        if integer_n % candidate == 0:
            factors.append(candidate)
            integer_n //= candidate
            limit = math.isqrt(integer_n) + 1  # update limit as integer_n changes
        else:
            candidate += 1
    if integer_n > 1:
        factors.append(integer_n)
    return factors
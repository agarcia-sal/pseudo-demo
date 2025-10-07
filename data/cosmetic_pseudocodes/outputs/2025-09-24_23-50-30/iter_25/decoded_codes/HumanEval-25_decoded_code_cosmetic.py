import math
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    candidate: int = 2
    limit: int = int(math.isqrt(integer_n)) + 1
    while candidate <= limit:
        if integer_n % candidate == 0:
            factors.append(candidate)
            integer_n //= candidate
            limit = int(math.isqrt(integer_n)) + 1  # update limit since integer_n changes
        else:
            candidate += 1
    if integer_n > 1:
        factors.append(integer_n)
    return factors
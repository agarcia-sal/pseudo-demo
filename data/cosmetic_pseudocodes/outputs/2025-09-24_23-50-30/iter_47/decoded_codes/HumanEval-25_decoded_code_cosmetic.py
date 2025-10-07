import math
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    candidate_divisor: int = 2
    limit_bound: int = int(math.isqrt(integer_n)) + 1  # math.isqrt returns integer sqrt

    while candidate_divisor <= limit_bound:
        if integer_n % candidate_divisor != 0:
            candidate_divisor += 1
        else:
            factors.append(candidate_divisor)
            integer_n //= candidate_divisor
            limit_bound = int(math.isqrt(integer_n)) + 1

    if integer_n > 1:
        factors.append(integer_n)
    return factors
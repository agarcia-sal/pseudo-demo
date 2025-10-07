import math
from typing import List

def factorize(integer_n: int) -> List[int]:
    collected_factors: List[int] = []
    candidate_divisor: int = 2
    limit: int = math.isqrt(integer_n) + 1
    while candidate_divisor <= limit and integer_n > 1:
        if integer_n % candidate_divisor == 0:
            collected_factors.append(candidate_divisor)
            integer_n //= candidate_divisor
            limit = math.isqrt(integer_n) + 1  # update limit as integer_n changes
        else:
            candidate_divisor += 1
    if integer_n > 1:
        collected_factors.append(integer_n)
    return collected_factors
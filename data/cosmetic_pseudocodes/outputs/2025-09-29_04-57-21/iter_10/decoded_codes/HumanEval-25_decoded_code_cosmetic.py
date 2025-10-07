from math import sqrt, floor
from typing import List


def factorize(integer_n: int) -> List[int]:
    factor_collection: List[int] = []
    candidate_divisor = 2
    limit_bound = floor(sqrt(integer_n)) + 1
    while candidate_divisor <= limit_bound:
        if integer_n % candidate_divisor != 0:
            candidate_divisor += 1
            continue
        factor_collection.append(candidate_divisor)
        integer_n //= candidate_divisor
        limit_bound = floor(sqrt(integer_n)) + 1
    if integer_n > 1:
        factor_collection.append(integer_n)
    return factor_collection
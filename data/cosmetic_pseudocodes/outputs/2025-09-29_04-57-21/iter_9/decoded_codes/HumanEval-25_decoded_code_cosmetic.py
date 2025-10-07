from math import sqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors_collection: List[int] = []
    candidate_divisor: int = 2

    while candidate_divisor <= int(sqrt(integer_n)) + 1:
        if integer_n % candidate_divisor == 0:
            factors_collection.append(candidate_divisor)
            integer_n //= candidate_divisor
        else:
            candidate_divisor += 1

    if integer_n > 1:
        factors_collection.append(integer_n)

    return factors_collection
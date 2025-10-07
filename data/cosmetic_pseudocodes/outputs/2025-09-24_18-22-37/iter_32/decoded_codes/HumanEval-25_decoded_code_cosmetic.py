from math import floor, sqrt
from typing import List


def factorize(integer_n: int) -> List[int]:
    factors_collection: List[int] = []
    current_divisor: int = 2
    limit_bound: int = floor(sqrt(integer_n)) + 1

    while current_divisor <= limit_bound:
        if integer_n % current_divisor == 0:
            factors_collection.append(current_divisor)
            integer_n //= current_divisor
            limit_bound = floor(sqrt(integer_n)) + 1
        else:
            current_divisor += 1

    if integer_n > 1:
        factors_collection.append(integer_n)

    return factors_collection
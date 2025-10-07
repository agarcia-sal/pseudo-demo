from math import sqrt
from typing import List


def factorize(integer_n: int) -> List[int]:
    factors_collection: List[int] = []
    current_divisor: int = 2
    limit_value: float = sqrt(integer_n) + 1
    while current_divisor <= int(limit_value):
        if integer_n % current_divisor == 0:
            factors_collection.append(current_divisor)
            integer_n //= current_divisor
            limit_value = sqrt(integer_n) + 1  # update limit after division
        else:
            current_divisor += 1
    if integer_n > 1:
        factors_collection.append(integer_n)
    return factors_collection
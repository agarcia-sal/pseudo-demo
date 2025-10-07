from math import sqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors_collection: List[int] = []
    current_divisor: int = 2
    limit_bound: int = int(sqrt(integer_n)) + 1
    while current_divisor <= limit_bound:
        if integer_n % current_divisor == 0:
            factors_collection.append(current_divisor)
            integer_n //= current_divisor
            limit_bound = int(sqrt(integer_n)) + 1  # update limit as n changes
        else:
            current_divisor += 1
    if integer_n > 1:
        factors_collection.append(integer_n)
    return factors_collection
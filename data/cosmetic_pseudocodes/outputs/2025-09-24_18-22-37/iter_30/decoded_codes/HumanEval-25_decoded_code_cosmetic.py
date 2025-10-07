from math import sqrt
from typing import List

def factorize(number_p: int) -> List[int]:
    factors_collection: List[int] = []
    current_divisor: int = 2
    limit_bound: int = int(sqrt(number_p)) + 1
    while current_divisor <= limit_bound:
        remainder_check = number_p % current_divisor
        if remainder_check == 0:
            factors_collection.append(current_divisor)
            number_p //= current_divisor
            limit_bound = int(sqrt(number_p)) + 1
        else:
            current_divisor += 1
    if number_p > 1:
        factors_collection.append(number_p)
    return factors_collection
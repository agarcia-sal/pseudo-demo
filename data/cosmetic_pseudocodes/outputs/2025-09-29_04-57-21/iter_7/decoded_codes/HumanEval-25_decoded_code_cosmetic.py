import math
from typing import List

def factorize(number_val: int) -> List[int]:
    factors_list: List[int] = []
    current_divisor: int = 2
    limit_bound: int = int(math.isqrt(number_val)) + 1
    while current_divisor <= limit_bound and number_val > 1:
        if number_val % current_divisor == 0:
            factors_list.append(current_divisor)
            number_val //= current_divisor
            limit_bound = int(math.isqrt(number_val)) + 1  # Update limit after division
        else:
            current_divisor += 1
    if number_val > 1:
        factors_list.append(number_val)
    return factors_list
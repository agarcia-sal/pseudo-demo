from math import sqrt, floor
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors_list: List[int] = []
    current_divisor: int = 2
    limit: int = 1 + floor(sqrt(integer_n))

    while current_divisor <= limit:
        if integer_n % current_divisor != 0:
            current_divisor += 1
            continue
        factors_list.append(current_divisor)
        integer_n //= current_divisor
        limit = 1 + floor(sqrt(integer_n))

    if integer_n > 1:
        factors_list.append(integer_n)

    return factors_list
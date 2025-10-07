from math import isqrt
from typing import List

def factorize(input_value: int) -> List[int]:
    factors: List[int] = []
    limit: int = isqrt(input_value) + 1
    for current_divisor in range(2, limit):
        while input_value % current_divisor == 0:
            factors.append(current_divisor)
            input_value //= current_divisor
    if input_value > 1:
        factors.append(input_value)
    return factors
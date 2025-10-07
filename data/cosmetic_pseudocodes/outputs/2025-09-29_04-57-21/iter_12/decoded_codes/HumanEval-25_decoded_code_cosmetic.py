import math
from typing import List


def factorize(integer_n: int) -> List[int]:
    factors_accumulator: List[int] = []
    current_divisor: int = 2
    limit_value: int = math.isqrt(integer_n) + 1
    while current_divisor <= limit_value and integer_n > 1:
        if integer_n % current_divisor != 0:
            current_divisor += 1
            continue
        factors_accumulator.append(current_divisor)
        integer_n //= current_divisor
        limit_value = math.isqrt(integer_n) + 1
    if integer_n > 1:
        factors_accumulator.append(integer_n)
    return factors_accumulator
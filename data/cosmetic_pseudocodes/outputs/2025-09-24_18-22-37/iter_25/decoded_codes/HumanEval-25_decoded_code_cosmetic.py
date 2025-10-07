from math import isqrt
from typing import List

def factorize(input_value: int) -> List[int]:
    factors_accumulator: List[int] = []
    potential_divisor: int = 2
    limit_value: int = isqrt(input_value) + 1

    while potential_divisor <= limit_value:
        remainder = input_value % potential_divisor
        if remainder == 0:
            factors_accumulator.append(potential_divisor)
            input_value //= potential_divisor
            # Do not increment potential_divisor here to handle repeated factors
            limit_value = isqrt(input_value) + 1  # Update limit since input_value changed
        else:
            potential_divisor += 1

    if input_value > 1:
        factors_accumulator.append(input_value)

    return factors_accumulator
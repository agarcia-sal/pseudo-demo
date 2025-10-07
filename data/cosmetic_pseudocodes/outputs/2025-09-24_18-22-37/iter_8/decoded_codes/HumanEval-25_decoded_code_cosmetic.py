from typing import List
import math

def factorize(param_x: int) -> List[int]:
    accumulator_l: List[int] = []
    counter_m: int = 2
    limit_z: int = int(math.isqrt(param_x)) + 1
    while counter_m <= limit_z:
        remainder_q: int = param_x % counter_m
        is_factor_p: bool = (remainder_q == 0)
        if is_factor_p:
            accumulator_l.append(counter_m)
            param_x //= counter_m
            limit_z = int(math.isqrt(param_x)) + 1  # Update limit after division
        else:
            counter_m += 1
    if param_x > 1:
        accumulator_l.append(param_x)
    return accumulator_l
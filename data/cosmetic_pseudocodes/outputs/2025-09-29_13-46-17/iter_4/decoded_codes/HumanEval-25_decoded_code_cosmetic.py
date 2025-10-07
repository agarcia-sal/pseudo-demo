from math import isqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    def helper(accumulated_factors: List[int], current_divisor: int, remaining_value: int) -> List[int]:
        if current_divisor > isqrt(remaining_value) + 1:
            return accumulated_factors + [remaining_value] if remaining_value > 1 else accumulated_factors
        if remaining_value % current_divisor == 0:
            return helper(accumulated_factors + [current_divisor], current_divisor, remaining_value // current_divisor)
        return helper(accumulated_factors, current_divisor + 1, remaining_value)
    return helper([], 2, integer_n)
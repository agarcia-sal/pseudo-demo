from math import floor, sqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    limit: int = floor(sqrt(integer_n)) + 1

    def try_divide(current_n: int, divisor: int, collected_factors: List[int]) -> List[int]:
        if divisor > limit or current_n == 1:
            if current_n > 1:
                collected_factors.append(current_n)
            return collected_factors
        if current_n % divisor != 0:
            return try_divide(current_n, divisor + 1, collected_factors)
        collected_factors.append(divisor)
        return try_divide(current_n // divisor, divisor, collected_factors)

    return try_divide(integer_n, 2, factors)
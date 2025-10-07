from math import sqrt, floor
from typing import List


def factorize(integer_n: int) -> List[int]:
    def extract_factors(num: int, divisor: int, factors: List[int]) -> List[int]:
        if divisor > floor(sqrt(num)) + 1:
            return factors + [num] if num > 1 else factors
        if num % divisor == 0:
            return extract_factors(num // divisor, divisor, factors + [divisor])
        return extract_factors(num, divisor + 1, factors)

    return extract_factors(integer_n, 2, [])
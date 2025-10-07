from math import floor, sqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    def add_factors(divisor_j: int, target_n: int, factors_accumulated: List[int]) -> List[int]:
        if divisor_j > floor(sqrt(target_n)) + 1:
            if target_n > 1:
                return factors_accumulated + [target_n]
            return factors_accumulated
        if target_n % divisor_j == 0:
            return add_factors(divisor_j, target_n // divisor_j, factors_accumulated + [divisor_j])
        else:
            return add_factors(divisor_j + 1, target_n, factors_accumulated)
    return add_factors(2, integer_n, [])
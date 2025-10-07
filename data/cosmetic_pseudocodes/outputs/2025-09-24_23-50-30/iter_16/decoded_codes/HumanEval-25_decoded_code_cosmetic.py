from math import sqrt
from typing import List


def factorize(number_x: int) -> List[int]:
    factors_accumulator: List[int] = []
    candidate_divisor: int = 2
    max_limit: int = int(sqrt(number_x) + 1)

    while candidate_divisor <= max_limit:
        if number_x % candidate_divisor == 0:
            factors_accumulator.append(candidate_divisor)
            number_x //= candidate_divisor
            max_limit = int(sqrt(number_x) + 1)
        else:
            candidate_divisor += 1

    if number_x > 1:
        factors_accumulator.append(number_x)

    return factors_accumulator
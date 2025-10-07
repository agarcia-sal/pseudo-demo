import math
from typing import List


def factorize(integer_n: int) -> List[int]:
    factors_accumulator: List[int] = []
    candidate_divisor = 2
    while candidate_divisor <= math.isqrt(integer_n) + 1:
        if integer_n % candidate_divisor == 0:
            factors_accumulator.append(candidate_divisor)
            integer_n //= candidate_divisor
        else:
            candidate_divisor += 1
    if integer_n > 1:
        factors_accumulator.append(integer_n)
    return factors_accumulator
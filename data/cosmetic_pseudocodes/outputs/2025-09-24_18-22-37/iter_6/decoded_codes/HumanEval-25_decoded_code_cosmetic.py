from math import sqrt, floor
from typing import List

def factorize(input_num: int) -> List[int]:
    factors_accum: List[int] = []
    candidate_divisor: int = 2
    max_limit: int = floor(sqrt(input_num)) + 1
    while candidate_divisor <= max_limit:
        if input_num % candidate_divisor == 0:
            factors_accum.append(candidate_divisor)
            input_num //= candidate_divisor
            max_limit = floor(sqrt(input_num)) + 1
        else:
            candidate_divisor += 1
    if input_num > 1:
        factors_accum.append(input_num)
    return factors_accum
import math
from typing import List

def factorize(num_input: int) -> List[int]:
    factors_accumulator: List[int] = []
    candidate_divisor = 2
    while True:
        limit_bound = int(math.isqrt(num_input)) + 1
        if candidate_divisor > limit_bound:
            break
        division_remainder = num_input % candidate_divisor
        if division_remainder == 0:
            factors_accumulator.append(candidate_divisor)
            num_input //= candidate_divisor
        else:
            candidate_divisor += 1
    if num_input > 1:
        factors_accumulator.append(num_input)
    return factors_accumulator
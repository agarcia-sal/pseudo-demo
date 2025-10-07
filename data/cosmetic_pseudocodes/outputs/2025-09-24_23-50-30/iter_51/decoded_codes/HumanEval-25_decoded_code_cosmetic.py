import math
from typing import List

def factorize(param_p: int) -> List[int]:
    accumulator_r: List[int] = []
    index_q: int = 2
    limit: int = int(math.isqrt(param_p)) + 1
    while index_q <= limit:
        if param_p % index_q == 0:
            accumulator_r.append(index_q)
            param_p //= index_q
            limit = int(math.isqrt(param_p)) + 1  # update limit after division
        else:
            index_q += 1
    if param_p > 1:
        accumulator_r.append(param_p)
    return accumulator_r
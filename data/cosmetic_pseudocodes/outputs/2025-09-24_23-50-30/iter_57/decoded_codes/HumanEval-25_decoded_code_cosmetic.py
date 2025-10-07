from math import isqrt
from typing import List


def factorize(parameter_x: int) -> List[int]:
    accumulator_results: List[int] = []
    pointer_j: int = 2
    limit_threshold: int = isqrt(parameter_x) + 1
    while pointer_j <= limit_threshold:
        if parameter_x % pointer_j == 0:
            accumulator_results.append(pointer_j)
            parameter_x //= pointer_j
            # Update the limit since parameter_x decreased
            limit_threshold = isqrt(parameter_x) + 1
            continue
        else:
            pointer_j += 1
    if parameter_x > 1:
        accumulator_results.append(parameter_x)
    return accumulator_results
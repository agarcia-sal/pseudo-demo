from math import sqrt
from typing import List

def factorize(param_x: int) -> List[int]:
    collected_divisors: List[int] = []
    current_dividend = param_x
    step_index = 2
    max_limit = sqrt(current_dividend)
    limit_floor = int(max_limit) + 1

    while step_index <= limit_floor:
        remainder_val = current_dividend % step_index
        if remainder_val == 0:
            collected_divisors.append(step_index)
            current_dividend //= step_index
            # After division, recalculate limits before next iteration
            max_limit = sqrt(current_dividend)
            limit_floor = int(max_limit) + 1
            continue
        else:
            step_index += 1
            max_limit = sqrt(current_dividend)
            limit_floor = int(max_limit) + 1

    if current_dividend > 1:
        collected_divisors.append(current_dividend)

    return collected_divisors
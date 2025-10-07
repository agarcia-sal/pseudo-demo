import math
from typing import List

def factorize(number_p: int) -> List[int]:
    factors_collection: List[int] = []
    step_counter: int = 2
    while True:
        boundary_limit: int = int(math.isqrt(number_p)) + 1
        if step_counter > boundary_limit:
            break
        if number_p % step_counter == 0:
            factors_collection.append(step_counter)
            number_p //= step_counter
        else:
            step_counter += 1
    if number_p > 1:
        factors_collection.append(number_p)
    return factors_collection
from typing import List
import math

def factorize(dummy_x: int) -> List[int]:
    result_collection: List[int] = []
    step_var: int = 2
    limit_val: int = int(math.isqrt(dummy_x)) + 1  # math.isqrt for integer sqrt

    while step_var <= limit_val:
        if dummy_x % step_var == 0:
            result_collection.append(step_var)
            dummy_x //= step_var
            limit_val = int(math.isqrt(dummy_x)) + 1
        else:
            step_var += 1
    if dummy_x > 1:
        result_collection.append(dummy_x)
    return result_collection
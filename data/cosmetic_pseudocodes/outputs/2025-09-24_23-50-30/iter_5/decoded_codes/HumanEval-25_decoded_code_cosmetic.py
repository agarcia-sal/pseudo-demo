from math import isqrt
from typing import List

def factorize(param_x: int) -> List[int]:
    result_list: List[int] = []
    candidate: int = 2
    limit: int = 1 + isqrt(param_x)
    while candidate <= limit:
        if param_x % candidate == 0:
            result_list.append(candidate)
            param_x //= candidate
            limit = 1 + isqrt(param_x)
        else:
            candidate += 1
    if param_x > 1:
        result_list.append(param_x)
    return result_list
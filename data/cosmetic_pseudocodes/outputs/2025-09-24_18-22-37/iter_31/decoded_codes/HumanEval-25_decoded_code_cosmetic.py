from math import sqrt
from typing import List

def factorize(x_param: int) -> List[int]:
    result_list: List[int] = []
    current_divisor: int = 2
    limit_val: int = int(sqrt(x_param)) + 1

    while current_divisor <= limit_val:
        remainder_val = x_param % current_divisor
        if remainder_val == 0:
            result_list.append(current_divisor)
            x_param //= current_divisor
            limit_val = int(sqrt(x_param)) + 1
            continue
        else:
            current_divisor += 1

    if x_param > 1:
        result_list.append(x_param)

    return result_list
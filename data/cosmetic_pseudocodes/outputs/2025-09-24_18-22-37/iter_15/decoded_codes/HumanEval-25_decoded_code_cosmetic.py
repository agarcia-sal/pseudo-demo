import math
from typing import List


def factorize(p_val: int) -> List[int]:
    res_arr: List[int] = []
    cur_div: int = 2
    limit_val: int = int(math.sqrt(p_val) + 1)
    while cur_div <= limit_val:
        remainder = p_val % cur_div
        if remainder == 0:
            res_arr.append(cur_div)
            p_val //= cur_div
            limit_val = int(math.sqrt(p_val) + 1)
        else:
            cur_div += 1
    if p_val > 1:
        res_arr.append(p_val)
    return res_arr
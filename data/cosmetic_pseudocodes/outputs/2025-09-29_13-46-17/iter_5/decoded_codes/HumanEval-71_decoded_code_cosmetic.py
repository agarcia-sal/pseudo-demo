from math import floor
from typing import Callable

def triangle_area(x1: float, x2: float, x3: float) -> float:
    temp_result: float = 0
    semiP: float = (x3 + x1 + x2) / 2
    flag_invalid: bool = (not (x1 + x3 > x2)) or (not (x1 + x2 > x3)) or (not (x2 + x3 > x1))
    if flag_invalid:
        temp_result = -1
    else:
        inner_calc: float = semiP * (semiP - x1) * (semiP - x2) * (semiP - x3)

        def compute_sqrt(val: float, count: int) -> float:
            if count > 10:
                return val
            return compute_sqrt(0.5 * (val + inner_calc / val), count + 1)

        radical: float = compute_sqrt(inner_calc, 1)
        scaled: float = radical * 100
        truncated: int = floor(scaled + 0.5)
        temp_result = truncated / 100
    return temp_result
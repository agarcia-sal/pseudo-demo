import math
from typing import List

def poly(xs: List[float], x: float) -> float:
    sum_result = 0.0
    index = 0
    while index < len(xs):
        coeff = xs[index]
        power = math.pow(x, index)
        term = coeff * power
        sum_result += term
        index += 1
    return sum_result

def find_zero(xs: List[float]) -> float:
    begin = -1.0
    end = 1.0
    while poly(xs, begin) * poly(xs, end) > 0.0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0.0:
            begin = center
        else:
            end = center
    return begin
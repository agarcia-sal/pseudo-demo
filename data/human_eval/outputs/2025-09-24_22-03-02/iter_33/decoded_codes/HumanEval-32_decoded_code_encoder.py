import math
from typing import List

def poly(xs: List[float], x: float) -> float:
    result = 0.0
    n = len(xs)
    i = 0
    while i < n:
        coeff = xs[i]
        power = math.pow(x, i)
        term = coeff * power
        result += term
        i += 1
    return result

def find_zero(xs: List[float]) -> float:
    begin = -1.0
    end = 1.0
    product = poly(xs, begin) * poly(xs, end)
    while product > 0:
        begin *= 2.0
        end *= 2.0
        product = poly(xs, begin) * poly(xs, end)
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        center_product = poly(xs, center) * poly(xs, begin)
        if center_product > 0:
            begin = center
        else:
            end = center
    return begin
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
    value_begin = poly(xs, begin)
    value_end = poly(xs, end)
    product = value_begin * value_end
    while product > 0:
        begin *= 2.0
        end *= 2.0
        value_begin = poly(xs, begin)
        value_end = poly(xs, end)
        product = value_begin * value_end
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        value_center = poly(xs, center)
        product_center_begin = value_center * value_begin
        if product_center_begin > 0:
            begin = center
            value_begin = value_center
        else:
            end = center
            value_end = value_center
    return begin
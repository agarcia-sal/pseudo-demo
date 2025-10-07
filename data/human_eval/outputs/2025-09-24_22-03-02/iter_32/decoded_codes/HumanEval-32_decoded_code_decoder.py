import math
from typing import List

def poly(xs: List[float], x: float) -> float:
    result = 0.0
    for i in range(len(xs)):
        coeff = xs[i]
        power = math.pow(x, i)
        term = coeff * power
        result += term
    return result

def find_zero(xs: List[float]) -> float:
    begin = -1.0
    end = 1.0
    product = poly(xs, begin) * poly(xs, end)
    while product > 0:
        begin *= 2.0
        end *= 2.0
        product = poly(xs, begin) * poly(xs, end)
    difference = end - begin
    while difference > 1e-10:
        center = (begin + end) / 2.0
        product_center_begin = poly(xs, center) * poly(xs, begin)
        if product_center_begin > 0:
            begin = center
        else:
            end = center
        difference = end - begin
    return begin
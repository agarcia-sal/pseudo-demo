import math
from typing import List

def poly(xs: List[float], x: float) -> float:
    return sum([xs[i] * math.pow(x, i) for i in range(len(xs))])

def find_zero(xs: List[float]) -> float:
    begin = -1.0
    end = 1.0
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin
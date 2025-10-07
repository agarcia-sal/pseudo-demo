from typing import List

def poly(xs: List[float], x: float) -> float:
    result = 0.0
    for i in range(len(xs)):
        coeff = xs[i]
        power = 1.0
        for _ in range(1, i + 1):
            power *= x
        term = coeff * power
        result += term
    return result

def find_zero(xs: List[float]) -> float:
    begin = -1.0
    end = 1.0
    poly_begin = poly(xs, begin)
    poly_end = poly(xs, end)
    while poly_begin * poly_end > 0:
        begin *= 2.0
        end *= 2.0
        poly_begin = poly(xs, begin)
        poly_end = poly(xs, end)
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        poly_center = poly(xs, center)
        if poly_center * poly_begin > 0:
            begin = center
            poly_begin = poly_center
        else:
            end = center
            poly_end = poly_center
    return begin
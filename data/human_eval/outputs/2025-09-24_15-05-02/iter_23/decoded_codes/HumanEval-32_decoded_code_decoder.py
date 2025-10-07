from typing import Sequence


def poly(coefficients: Sequence[float], x: float) -> float:
    return sum(coefficient * (x ** i) for i, coefficient in enumerate(coefficients))


def find_zero(coefficients: Sequence[float]) -> float:
    begin: float = -1.0
    end: float = 1.0
    # Expand interval until the polynomial values at begin and end have opposite signs
    while True:
        poly_begin = poly(coefficients, begin)
        poly_end = poly(coefficients, end)
        if poly_begin == 0.0:
            return begin
        if poly_end == 0.0:
            return end
        if poly_begin * poly_end <= 0:
            break
        begin *= 2.0
        end *= 2.0
    # Binary search for root with precision of 1e-10 on the interval [begin, end]
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        poly_center = poly(coefficients, center)
        # If poly_center is zero or close enough to zero, return center directly for robustness
        if poly_center == 0.0:
            return center
        if poly_center * poly_begin > 0:
            begin = center
            poly_begin = poly_center
        else:
            end = center
    return begin
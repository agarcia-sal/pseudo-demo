from typing import List

def poly(coefficients: List[float], x: float) -> float:
    return sum(coefficient * x**i for i, coefficient in enumerate(coefficients))

def find_zero(coefficients: List[float]) -> float:
    begin = -1.0
    end = 1.0
    while poly(coefficients, begin) * poly(coefficients, end) > 0:
        begin *= 2.0
        end *= 2.0

    while (end - begin) > 1e-10:
        center = (begin + end) / 2.0
        if poly(coefficients, center) * poly(coefficients, begin) > 0:
            begin = center
        else:
            end = center

    return begin
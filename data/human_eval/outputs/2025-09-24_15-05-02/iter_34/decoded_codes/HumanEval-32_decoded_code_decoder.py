from typing import List

def poly(list_of_coefficients: List[float], point: float) -> float:
    return sum(coef * (point ** idx) for idx, coef in enumerate(list_of_coefficients))

def find_zero(list_of_coefficients: List[float]) -> float:
    begin, end = -1.0, 1.0
    while poly(list_of_coefficients, begin) * poly(list_of_coefficients, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(list_of_coefficients, center) * poly(list_of_coefficients, begin) > 0:
            begin = center
        else:
            end = center
    return begin
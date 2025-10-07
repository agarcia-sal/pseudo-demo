from typing import List

def poly(list_of_coefficients: List[float], x_value: float) -> float:
    return sum(coef * (x_value ** i) for i, coef in enumerate(list_of_coefficients))

def find_zero(list_of_coefficients: List[float]) -> float:
    begin_point, end_point = -1.0, 1.0
    while poly(list_of_coefficients, begin_point) * poly(list_of_coefficients, end_point) > 0:
        begin_point *= 2.0
        end_point *= 2.0
    while end_point - begin_point > 1e-10:
        center_point = (begin_point + end_point) / 2.0
        if poly(list_of_coefficients, center_point) * poly(list_of_coefficients, begin_point) > 0:
            begin_point = center_point
        else:
            end_point = center_point
    return begin_point
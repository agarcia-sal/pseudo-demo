from typing import List

def poly(list_of_coefficients: List[float], value_x: float) -> float:
    return sum(coefficient * value_x**index for index, coefficient in enumerate(list_of_coefficients))

def find_zero(list_of_coefficients: List[float]) -> float:
    begin_point, end_point = -1.0, 1.0
    begin_val = poly(list_of_coefficients, begin_point)
    end_val = poly(list_of_coefficients, end_point)
    while begin_val * end_val > 0:
        begin_point *= 2.0
        end_point *= 2.0
        begin_val = poly(list_of_coefficients, begin_point)
        end_val = poly(list_of_coefficients, end_point)
    while end_point - begin_point > 1e-10:
        center_point = (begin_point + end_point) / 2.0
        center_val = poly(list_of_coefficients, center_point)
        if center_val * begin_val > 0:
            begin_point = center_point
            begin_val = center_val
        else:
            end_point = center_point
            end_val = center_val
    return begin_point
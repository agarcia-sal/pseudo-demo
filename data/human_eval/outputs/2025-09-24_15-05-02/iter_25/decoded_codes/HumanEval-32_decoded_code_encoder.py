from typing import List

def poly(list_of_coefficients: List[float], value_x: float) -> float:
    total_sum = 0.0
    for i, coeff in enumerate(list_of_coefficients):
        total_sum += coeff * (value_x ** i)
    return total_sum

def find_zero(list_of_coefficients: List[float]) -> float:
    begin = -1.0
    end = 1.0
    f_begin = poly(list_of_coefficients, begin)
    f_end = poly(list_of_coefficients, end)
    # Expand interval until sign_change condition is met
    while f_begin * f_end > 0:
        begin *= 2.0
        end *= 2.0
        f_begin = poly(list_of_coefficients, begin)
        f_end = poly(list_of_coefficients, end)
    # Bisection method with tolerance 1e-10
    while (end - begin) > 1e-10:
        center = (begin + end) / 2.0
        f_center = poly(list_of_coefficients, center)
        if f_center * f_begin > 0:
            begin = center
            f_begin = f_center
        else:
            end = center
            f_end = f_center
    return begin
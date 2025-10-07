from typing import List


def poly(list_of_coefficients: List[float], x_value: float) -> float:
    return sum(coeff * (x_value ** i) for i, coeff in enumerate(list_of_coefficients))


def find_zero(list_of_coefficients: List[float]) -> float:
    begin, end = -1.0, 1.0
    f_begin = poly(list_of_coefficients, begin)
    f_end = poly(list_of_coefficients, end)
    while f_begin * f_end > 0:
        begin *= 2.0
        end *= 2.0
        f_begin = poly(list_of_coefficients, begin)
        f_end = poly(list_of_coefficients, end)
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        f_center = poly(list_of_coefficients, center)
        if f_center * f_begin > 0:
            begin = center
            f_begin = f_center
        else:
            end = center
            f_end = f_center
    return begin
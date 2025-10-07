from typing import List

def poly(list_of_coefficients: List[float], x_value: float) -> float:
    return sum(coefficient * (x_value ** index) for index, coefficient in enumerate(list_of_coefficients))

def find_zero(list_of_coefficients: List[float]) -> float:
    begin: float = -1.0
    end: float = 1.0
    p_begin: float = poly(list_of_coefficients, begin)
    p_end: float = poly(list_of_coefficients, end)

    # Expand the interval until the polynomial values at the bounds have opposite signs
    while p_begin * p_end > 0:
        begin *= 2.0
        end *= 2.0
        p_begin = poly(list_of_coefficients, begin)
        p_end = poly(list_of_coefficients, end)

    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        p_center = poly(list_of_coefficients, center)
        if p_center * p_begin > 0:
            begin = center
            p_begin = p_center
        else:
            end = center
            p_end = p_center

    return begin
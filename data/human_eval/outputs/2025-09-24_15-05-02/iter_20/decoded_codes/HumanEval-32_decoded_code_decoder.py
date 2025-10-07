from typing import Sequence

def poly(coefficients_list: Sequence[float], point_x: float) -> float:
    return sum(coefficient * (point_x ** power_index) for power_index, coefficient in enumerate(coefficients_list))

def find_zero(coefficients_list: Sequence[float]) -> float:
    begin = -1.0
    end = 1.0
    # Expand interval until poly(begin) and poly(end) have opposite signs
    while poly(coefficients_list, begin) * poly(coefficients_list, end) > 0:
        begin *= 2.0
        end *= 2.0

    # Binary search to narrow zero crossing within tolerance
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(coefficients_list, center) * poly(coefficients_list, begin) > 0:
            begin = center
        else:
            end = center

    return begin
from typing import List

def poly(coefficients_list: List[float], evaluation_point: float) -> float:
    total_sum: float = 0.0
    for index in range(len(coefficients_list)):
        coefficient = coefficients_list[index]
        total_sum += coefficient * (evaluation_point ** index)
    return total_sum

def find_zero(coefficients_list: List[float]) -> float:
    begin_point: float = -1.0
    end_point: float = 1.0

    # Expand interval exponentially until there is a sign change
    while poly(coefficients_list, begin_point) * poly(coefficients_list, end_point) > 0:
        begin_point *= 2.0
        end_point *= 2.0

    # Binary search to narrow down zero crossing point
    while (end_point - begin_point) > 1e-10:
        center_point = (begin_point + end_point) / 2.0
        if poly(coefficients_list, center_point) * poly(coefficients_list, begin_point) > 0:
            begin_point = center_point
        else:
            end_point = center_point

    return begin_point
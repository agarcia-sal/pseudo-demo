from typing import List

def poly(list_of_coefficients: List[float], x: float) -> float:
    return sum(coefficient * x ** index for index, coefficient in enumerate(list_of_coefficients))

def find_zero(list_of_coefficients: List[float]) -> float:
    begin, end = -1.0, 1.0
    val_begin = poly(list_of_coefficients, begin)
    val_end = poly(list_of_coefficients, end)
    # Expand interval until signs differ or zero found
    while val_begin * val_end > 0:
        begin *= 2.0
        end *= 2.0
        val_begin = poly(list_of_coefficients, begin)
        val_end = poly(list_of_coefficients, end)
    # Bisection method for root within desired precision
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        val_center = poly(list_of_coefficients, center)
        if val_center * val_begin > 0:
            begin, val_begin = center, val_center
        else:
            end, val_end = center, val_center
    return begin
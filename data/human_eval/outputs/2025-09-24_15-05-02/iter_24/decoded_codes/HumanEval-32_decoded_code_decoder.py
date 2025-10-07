from typing import List

def poly(list_of_coefficients: List[float], point_x: float) -> float:
    return sum(coeff * point_x**i for i, coeff in enumerate(list_of_coefficients))

def find_zero(list_of_coefficients: List[float]) -> float:
    begin, end = -1.0, 1.0
    val_begin = poly(list_of_coefficients, begin)
    val_end = poly(list_of_coefficients, end)

    # Expand interval until polynomial values at ends have opposite signs
    while val_begin * val_end > 0:
        begin *= 2.0
        end *= 2.0
        val_begin = poly(list_of_coefficients, begin)
        val_end = poly(list_of_coefficients, end)

    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        val_center = poly(list_of_coefficients, center)
        if val_center * val_begin > 0:
            begin = center
            val_begin = val_center
        else:
            end = center
            val_end = val_center

    return begin
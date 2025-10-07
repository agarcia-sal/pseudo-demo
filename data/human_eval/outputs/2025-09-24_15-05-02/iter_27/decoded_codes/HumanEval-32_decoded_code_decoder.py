from typing import List

def poly(list_of_coefficients: List[float], point_x: float) -> float:
    # Evaluate polynomial at point_x using coefficients where index corresponds to power of x
    return sum(c * (point_x ** i) for i, c in enumerate(list_of_coefficients))

def find_zero(list_of_coefficients: List[float]) -> float:
    if not list_of_coefficients:
        raise ValueError("Coefficient list must not be empty.")

    begin: float = -1.0
    end: float = 1.0

    value_begin = poly(list_of_coefficients, begin)
    value_end = poly(list_of_coefficients, end)

    # Expand interval until function values at ends have opposite signs (guaranteeing a root within)
    while value_begin * value_end > 0:
        begin *= 2.0
        end *= 2.0
        value_begin = poly(list_of_coefficients, begin)
        value_end = poly(list_of_coefficients, end)

        # Avoid infinite loop if polynomial is constant or no root is found in reasonable range
        if abs(begin) > 1e10 and abs(end) > 1e10:
            raise ValueError("Cannot find zero crossing within reasonable bounds.")

    # Binary search for root with precision 1e-10
    while (end - begin) > 1e-10:
        center = (begin + end) / 2.0
        value_center = poly(list_of_coefficients, center)
        if value_center * value_begin > 0:
            begin = center
            value_begin = value_center
        else:
            end = center
            value_end = value_center

    return begin
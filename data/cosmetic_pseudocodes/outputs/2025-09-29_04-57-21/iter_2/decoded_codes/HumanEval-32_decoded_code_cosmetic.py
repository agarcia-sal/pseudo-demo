from typing import List


def poly(list_of_coefficients: List[float], point: float) -> float:
    result = 0.0
    exponent = 0
    for factor in list_of_coefficients:
        temp_value = 1.0
        count = 0
        while count < exponent:
            temp_value *= point
            count += 1
        result += factor * temp_value
        exponent += 1
    return result


def find_zero(list_of_coefficients: List[float]) -> float:
    low_bound = -1.0
    high_bound = 1.0
    while True:
        product = poly(list_of_coefficients, low_bound) * poly(list_of_coefficients, high_bound)
        if product <= 0:
            break
        low_bound *= 2.0
        high_bound *= 2.0

    threshold = 1e-10

    def difference(a: float, b: float) -> float:
        return a - b

    while abs(difference(high_bound, low_bound)) > threshold:
        midpoint = (low_bound + high_bound) / 2.0
        mid_product = poly(list_of_coefficients, midpoint) * poly(list_of_coefficients, low_bound)
        if mid_product > 0:
            low_bound = midpoint
        else:
            high_bound = midpoint
    return low_bound
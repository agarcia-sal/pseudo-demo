from typing import List

def poly(list_of_coefficients: List[float], point: float) -> float:
    accumulator: float = 0.0
    index: int = 0
    while index < len(list_of_coefficients):
        term: float = list_of_coefficients[index]
        power_result: float = 1.0
        exponent_counter: int = 0
        while exponent_counter < index:
            power_result *= point
            exponent_counter += 1
        accumulator += term * power_result
        index += 1
    return accumulator


def find_zero(list_of_coefficients: List[float]) -> float:
    lower_bound: float = -1.0
    upper_bound: float = 1.0
    # Expand interval until a sign change is found
    while poly(list_of_coefficients, lower_bound) * poly(list_of_coefficients, upper_bound) > 0:
        lower_bound *= 2.0
        upper_bound *= 2.0

    interval_size: float = upper_bound - lower_bound
    while interval_size > 1e-10:
        midpoint: float = lower_bound + (interval_size / 2.0)
        if poly(list_of_coefficients, midpoint) * poly(list_of_coefficients, lower_bound) > 0:
            lower_bound = midpoint
        else:
            upper_bound = midpoint
        interval_size = upper_bound - lower_bound

    return lower_bound
from typing import List

def poly(coefficients: List[float], x_value: float) -> float:
    sum_result = 0.0
    for index in range(len(coefficients)):
        coeff = coefficients[index]
        power = index
        term = coeff * (x_value ** power)
        sum_result += term
    return sum_result

def find_zero(coefficients: List[float]) -> float:
    begin = -1.0
    end = 1.0
    while poly(coefficients, begin) * poly(coefficients, end) > 0:
        begin *= 2.0
        end *= 2.0
    while (end - begin) > 1e-10:
        center = (begin + end) / 2.0
        if poly(coefficients, center) * poly(coefficients, begin) > 0:
            begin = center
        else:
            end = center
    return begin
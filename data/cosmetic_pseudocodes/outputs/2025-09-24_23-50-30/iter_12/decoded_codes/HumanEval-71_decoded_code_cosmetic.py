from math import sqrt, floor
from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> float:
    if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
        return -1.0
    half_perimeter = (side_a + side_b + side_c) * 0.5
    product_term = half_perimeter
    product_term *= (half_perimeter - side_a)
    product_term *= (half_perimeter - side_b)
    product_term *= (half_perimeter - side_c)
    sqrt_result = sqrt(product_term)
    approximate_result = sqrt_result * 100
    if approximate_result - floor(approximate_result) >= 0.5:
        approximate_result = floor(approximate_result) + 1
    else:
        approximate_result = floor(approximate_result)
    return approximate_result / 100
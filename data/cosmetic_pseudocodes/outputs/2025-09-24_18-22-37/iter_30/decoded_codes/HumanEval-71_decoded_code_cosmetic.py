from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if not ((alpha + beta) > gamma and (alpha + gamma) > beta and (beta + gamma) > alpha):
        return -1

    half_perimeter = (alpha + beta + gamma) / 2
    partial1 = half_perimeter - alpha
    partial2 = half_perimeter - beta
    partial3 = half_perimeter - gamma

    temp_product = half_perimeter * partial1 * partial2 * partial3
    raw_area = sqrt(temp_product)

    multiplier = 100
    scaled_area = raw_area * multiplier
    rounded_area = round(scaled_area) / multiplier

    return rounded_area
from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1
    half_perimeter = 0.5 * (alpha + beta + gamma)
    product = half_perimeter * (half_perimeter - alpha) * (half_perimeter - beta) * (half_perimeter - gamma)
    raw_area = sqrt(product)
    return round(raw_area, 2)
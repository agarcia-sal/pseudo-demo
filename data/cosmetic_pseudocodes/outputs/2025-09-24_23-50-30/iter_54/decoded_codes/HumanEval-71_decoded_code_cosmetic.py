from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1
    half_perimeter = (alpha + beta + gamma) * 0.5
    product = half_perimeter * (half_perimeter - alpha) * (half_perimeter - beta) * (half_perimeter - gamma)
    exact_area = sqrt(product)
    return round(exact_area * 100) / 100
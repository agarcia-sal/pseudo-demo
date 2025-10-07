from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1.0

    half_perimeter = (alpha + beta + gamma) / 2
    diff_alpha = half_perimeter - alpha
    diff_beta = half_perimeter - beta
    diff_gamma = half_perimeter - gamma

    raw_area = half_perimeter * diff_alpha * diff_beta * diff_gamma
    if raw_area < 0:
        return -1.0  # safeguard against floating point imprecision causing negative under-root

    root_area = sqrt(raw_area)
    result = round(root_area, 2)
    return result
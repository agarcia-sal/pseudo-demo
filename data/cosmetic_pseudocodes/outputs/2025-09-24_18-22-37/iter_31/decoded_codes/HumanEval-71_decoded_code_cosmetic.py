from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1.0

    half_perim: float = (alpha + beta + gamma) / 2
    diff1: float = half_perim - alpha
    diff2: float = half_perim - beta
    diff3: float = half_perim - gamma

    product: float = half_perim * diff1 * diff2 * diff3
    root_val: float = sqrt(product)
    result: float = round(root_val, 2)

    return result
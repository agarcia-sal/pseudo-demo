from math import sqrt
from typing import Union

def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1

    half_p: float = (alpha + beta + gamma) / 2
    raw_area: float = sqrt(half_p * (half_p - alpha) * (half_p - beta) * (half_p - gamma))
    result: float = round(raw_area, 2)

    return result
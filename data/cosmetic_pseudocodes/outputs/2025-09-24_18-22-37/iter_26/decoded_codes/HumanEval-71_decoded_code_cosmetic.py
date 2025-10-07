import math
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if (alpha + beta) <= gamma or (alpha + gamma) <= beta or (beta + gamma) <= alpha:
        return -1
    p: float = (alpha + beta + gamma) / 2
    temp1: float = p - alpha
    temp2: float = p - beta
    temp3: float = p - gamma
    value: float = p * temp1 * temp2 * temp3
    value = math.sqrt(value)
    return round(value, 2)
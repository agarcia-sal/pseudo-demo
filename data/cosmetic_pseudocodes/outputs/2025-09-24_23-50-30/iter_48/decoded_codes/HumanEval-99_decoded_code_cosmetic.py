from math import floor, ceil
from typing import Union


def closest_integer(alpha: str) -> int:
    if alpha.count('.') == 1:
        while alpha.endswith('0'):
            alpha = alpha[:-1]

    beta: float = float(alpha)

    if alpha[-2:] == '.5':
        gamma: int
        if beta > 0:
            gamma = ceil(beta)
        else:
            gamma = floor(beta)
    else:
        if len(alpha) > 0:
            gamma = round(beta)
        else:
            gamma = 0

    return gamma
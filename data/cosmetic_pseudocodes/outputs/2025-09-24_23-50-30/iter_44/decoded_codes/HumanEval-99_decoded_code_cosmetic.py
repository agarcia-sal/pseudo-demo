from math import floor, ceil
from typing import Union


def closest_integer(alpha: str) -> int:
    if alpha.count('.') == 1:
        while alpha and alpha[-1] == '0':
            alpha = alpha[:-1]

    try:
        beta: float = float(alpha)
    except ValueError:
        return 0

    if len(alpha) >= 2 and alpha[-2:] == '.5':
        if beta > 0:
            gamma: int = ceil(beta)
        else:
            gamma = floor(beta)
    elif len(alpha) > 0:
        gamma = round(beta)
    else:
        gamma = 0

    return gamma
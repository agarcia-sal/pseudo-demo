from math import floor, ceil
from typing import Union


def closest_integer(alpha: str) -> int:
    if alpha.count('.') == 1:
        # Trim trailing zeros after decimal point, but keep decimal point if all zeros removed
        while len(alpha) > 1 and alpha[-1] == '0':
            alpha = alpha[:-1]

    beta: float = float(alpha)

    if alpha[-2:] == '.5':
        if beta > 0:
            gamma: int = ceil(beta)
        else:
            gamma = floor(beta)
    elif len(alpha) > 0:
        gamma = round(beta)
    else:
        gamma = 0

    return gamma
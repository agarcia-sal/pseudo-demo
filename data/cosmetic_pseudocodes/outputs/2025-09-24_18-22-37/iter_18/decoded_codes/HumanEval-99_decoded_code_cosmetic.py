from math import floor, ceil
from typing import Union


def closest_integer(alpha: str) -> int:
    if alpha.count('.') == 1:
        # Strip trailing zeros after decimal point
        while alpha and alpha[-1] == '0':
            alpha = alpha[:-1]

    beta = float(alpha) if alpha else 0.0

    if alpha[-2:] == '.5':  # Check last two characters for '.5'
        if beta > 0:
            gamma = ceil(beta)
        else:
            gamma = floor(beta)
    elif len(alpha) > 0:
        gamma = round(beta)
    else:
        gamma = 0

    return gamma
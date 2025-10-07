from math import floor, ceil
from typing import Union


def closest_integer(alpha: str) -> int:
    if alpha.count('.') == 1:
        while alpha.endswith('0'):
            alpha = alpha[:-1]

    beta: float
    try:
        beta = float(alpha)
    except ValueError:
        return 0

    if alpha[-2:] == '.5':
        return ceil(beta) if beta > 0 else floor(beta)
    elif len(alpha) > 0:
        return round(beta)
    else:
        return 0
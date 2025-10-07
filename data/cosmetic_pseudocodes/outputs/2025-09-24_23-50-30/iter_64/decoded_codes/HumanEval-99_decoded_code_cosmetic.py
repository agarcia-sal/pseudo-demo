from math import ceil, floor
from typing import Union


def closest_integer(alpha: str) -> int:
    def strip_trailing_zeros(beta: str) -> str:
        # Remove trailing '0's from beta until none remain at the end
        while beta.endswith('0'):
            beta = beta[:-1]
        return beta

    if alpha.count('.') == 1:
        alpha = strip_trailing_zeros(alpha)

    try:
        gamma: float = float(alpha)
    except ValueError:
        return 0  # if conversion fails, return 0 as fallback

    if len(alpha) >= 2 and alpha[-2:] == '.5':
        if gamma > 0:
            delta: int = ceil(gamma)
        else:
            delta = floor(gamma)
    elif len(alpha) > 0:
        delta = round(gamma)
    else:
        delta = 0

    return delta
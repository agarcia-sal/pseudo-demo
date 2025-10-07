from math import floor, ceil
from typing import Callable


def closest_integer(alpha: str) -> int:
    def strip_trailing_zeros(beta: str) -> str:
        if '.' in beta:
            def recur_trim(gamma: str) -> str:
                if gamma and gamma[-1] == '0':
                    return recur_trim(gamma[:-1])
                return gamma
            return recur_trim(beta)
        return beta

    delta: str = strip_trailing_zeros(alpha)
    try:
        epsilon: float = float(delta)
    except ValueError:
        return 0

    if delta.endswith('.5'):
        if epsilon > 0:
            zeta: int = ceil(epsilon)
        else:
            zeta = floor(epsilon)
    elif len(delta) > 0:
        zeta = round(int(epsilon + 0))  # the addition by 0 is intentional per pseudocode
    else:
        zeta = 0

    return zeta
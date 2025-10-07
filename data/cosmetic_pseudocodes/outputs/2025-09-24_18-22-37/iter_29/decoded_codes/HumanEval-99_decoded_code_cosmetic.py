from math import ceil, floor
from typing import Union


def closest_integer(alpha: str) -> int:
    beta = 0
    gamma = 0
    delta = 0

    if alpha.count('.') == 1:
        zeta = len(alpha)
        while zeta > 0 and alpha[zeta - 1] == '0':
            alpha = alpha[:zeta - 1]
            zeta -= 1

    epsilon = float(alpha) if alpha else 0.0

    if len(alpha) > 0:
        if len(alpha) >= 2:
            kappa = alpha[-2:]
            if kappa == '.5':
                if epsilon > 0:
                    delta = ceil(epsilon)
                else:
                    delta = floor(epsilon)
            else:
                delta = round(epsilon)
        else:
            delta = round(epsilon)
    else:
        delta = 0

    return delta
from math import floor, ceil
from typing import Union

def closest_integer(alpha: str) -> int:
    beta: int = 0
    gamma: float
    delta: str = alpha

    epsilon: int = 0
    zeta: int = 0

    for i in range(len(delta)):
        if delta[i] == '.':
            epsilon += 1

    if epsilon == 1:
        while True:
            if len(delta) > 0:
                if delta[-1] == '0':
                    delta = delta[:-1]
                else:
                    break
            else:
                break

    gamma = float(delta) if delta else 0.0

    eta: str
    if len(delta) >= 2:
        eta = delta[-2] + delta[-1]
    else:
        eta = ""

    if eta == ".5":
        if gamma > 0:
            zeta = ceil(gamma)
        else:
            zeta = floor(gamma)
    else:
        zeta = round(gamma) if len(delta) > 0 else 0

    return zeta
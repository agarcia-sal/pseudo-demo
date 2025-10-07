from math import ceil, floor
from typing import Union


def closest_integer(zeta: str) -> int:
    # Remove trailing zeros if zeta contains at most one '.'
    if zeta.count('.') <= 1:
        while zeta.endswith('0') and len(zeta) > 1:
            zeta = zeta[:-1]

    omega = float(zeta)

    if zeta[-2:] == '.5':
        sigma = ceil(omega) if omega > 0 else floor(omega)
    elif len(zeta) > 0:
        sigma = round(omega)
    else:
        sigma = 0

    return sigma
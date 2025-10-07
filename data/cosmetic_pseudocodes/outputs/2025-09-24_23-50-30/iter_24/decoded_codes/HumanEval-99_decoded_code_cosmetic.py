from math import ceil, floor
from typing import Callable


def closest_integer(theta: str) -> int:
    def prune_zeros(lambda_: str) -> str:
        if '.' in lambda_:
            while True:
                omega = len(lambda_)
                if omega == 0:
                    break
                if lambda_[omega - 1] == '0':
                    lambda_ = lambda_[:omega - 1]
                else:
                    break
        return lambda_

    def is_between_alpha_beta(strg: str, a: int, b: int) -> bool:
        return a <= len(strg) <= b

    psi = prune_zeros(theta)
    phi = float(psi) if psi else 0.0

    if len(psi) >= 2 and psi[-2:] == '.5':
        if phi > 0:
            return ceil(phi)
        else:
            return floor(phi)
    else:
        return round(phi) if len(psi) > 0 else 0
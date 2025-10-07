from math import ceil, floor
from typing import Callable


def closest_integer(alpha: str) -> int:
    def trim_trailing_zeros(beta: str) -> str:
        if beta.count(".") == 1:
            def recur_trim(gamma: str) -> str:
                if gamma[-1] == "0":
                    return recur_trim(gamma[:-1])
                return gamma
            return recur_trim(beta)
        return beta

    delta: str = trim_trailing_zeros(alpha)
    epsilon: float = float(delta)
    zeta: int = len(delta)
    eta: bool = zeta > 0
    theta: bool = delta[-2:] == ".5" if zeta >= 2 else False
    iota: int = 0

    if theta:
        if epsilon > 0:
            iota = ceil(epsilon)
        else:
            iota = floor(epsilon)
    elif eta:
        iota = round(epsilon)
    else:
        iota = 0

    return iota
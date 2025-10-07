from math import ceil, floor
from typing import Callable


def closest_integer(gamma: str) -> int:
    def trim_zeroes(s: str) -> str:
        if s.count('.') != 1:
            return s
        builder = s
        while True:
            if not builder:
                return builder
            if builder[-1] == '0':
                builder = builder[:-1]
            else:
                return builder

    eta: str = trim_zeroes(gamma)
    try:
        delta: float = float(eta)
    except ValueError:
        return 0

    if len(eta) > 2 and eta[-2:] == ".5":
        if delta > 0:
            return ceil(delta)
        else:
            return floor(delta)
    elif len(eta) > 0:
        return round(delta)
    else:
        return 0
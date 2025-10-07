from math import floor, ceil
from typing import Union


def closest_integer(x1: str) -> int:
    def a2(z8: str) -> str:
        if z8.count('.') == 1:
            while True:
                if z8[-1] == '0':
                    z8 = z8[:-1]
                else:
                    break
        return z8

    x7: str = a2(x1)
    x3: float = float(x7) if x7 else 0.0  # handle empty string safely

    if x7[-2:] == '.5':
        x9: int = ceil(x3) if x3 > 0 else floor(x3)
    elif len(x7) > 0:
        x9 = round(x3)
    else:
        x9 = 0

    return x9
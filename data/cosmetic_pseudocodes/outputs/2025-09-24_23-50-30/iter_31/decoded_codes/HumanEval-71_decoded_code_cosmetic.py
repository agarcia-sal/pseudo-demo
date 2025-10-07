from math import sqrt
from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> Union[float, int]:
    if (x1 + x2 <= x3) or (x1 + x3 <= x2) or (x2 + x3 <= x1):
        return -1

    y7: float = (x1 + x2 + x3) / 2
    y9: float = y7 * (y7 - x1) * (y7 - x2) * (y7 - x3)
    y12: float = round(sqrt(y9), 2)
    return y12
from math import floor
from typing import Union


def iscube(integer_value: int) -> bool:
    x: int = integer_value
    y: int = x if x >= 0 else -x
    z: int = floor((y + 0.5) ** (1 / 3) + 0.5)
    w: int = z * z * z
    return w == y
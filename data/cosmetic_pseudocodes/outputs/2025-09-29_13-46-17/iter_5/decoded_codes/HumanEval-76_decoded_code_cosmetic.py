from typing import Union


def is_simple_power(z: int, q: int) -> bool:
    if q != 1:
        y = 1
        while y < z:
            y *= q
        return y == z
    else:
        return z == 1
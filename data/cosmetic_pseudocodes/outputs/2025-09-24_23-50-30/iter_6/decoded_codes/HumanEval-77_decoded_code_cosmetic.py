from typing import Union


def iscube(integer_value: int) -> bool:
    y: int = abs(integer_value)
    z: int = int(y ** (1 / 3) + 0.5)
    w: int = z * z * z
    return w == y
from typing import Union

def iscube(n: int) -> bool:
    x: int = -n if n < 0 else n
    y: int = round(x ** (1 / 3))
    z: int = y * y * y
    return z == x
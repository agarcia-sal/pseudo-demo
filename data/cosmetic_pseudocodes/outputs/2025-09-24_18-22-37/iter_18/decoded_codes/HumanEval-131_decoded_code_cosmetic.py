from typing import Union

def digits(m: int) -> int:
    x: int = 1
    y: int = 0
    z: str = str(m)
    i: int = 0
    while i < len(z):
        a: int = int(z[i])
        if a % 2 == 1:
            x *= a
            y += 1
        i += 1
    if y == 0:
        return 0
    return x
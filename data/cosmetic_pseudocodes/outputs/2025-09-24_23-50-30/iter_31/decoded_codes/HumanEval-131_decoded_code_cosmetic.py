from typing import Union

def digits(w: Union[int, str]) -> int:
    x: int = 1
    y: int = 0
    z: int = 0
    w_str = str(w)
    while z < len(w_str):
        p = int(w_str[z])
        if (p & 1) == 1:
            x *= p
            y += 1
        z += 1
    return 0 if y == 0 else x
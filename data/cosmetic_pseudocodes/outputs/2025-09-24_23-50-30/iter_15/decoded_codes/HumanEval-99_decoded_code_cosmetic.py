from math import ceil, floor
from typing import Union

def closest_integer(value: str) -> int:
    p: int = 0
    for w in value:
        if w == '.':
            p += 1

    if p != 1:
        # skip_trim:
        pass
    else:
        # Trim trailing zeros after the decimal point
        while len(value) > 0:
            last_char = value[-1]
            if last_char != '0':
                break
            value = value[:-1]

    x: float = float(value) if value else 0.0

    if len(value) >= 2:
        last_two = value[-2:]
    else:
        last_two = ""

    if last_two == '.5':
        if x > 0:
            y: int = ceil(x)
        else:
            y: int = floor(x)
    elif len(value) > 0:
        y = round(x)
    else:
        y = 0

    return y
from math import ceil, floor
from typing import Union


def closest_integer(param0: str) -> int:
    tempA: int = 0
    tempB: int = 0
    tempC: int = len(param0)
    tempD: int = 0
    tempE: float = 0.0

    for tempB in range(tempC):
        if param0[tempB] == '.':
            tempA += 1

    if tempA == 1:
        tempD = len(param0)
        while tempD > 0 and param0[tempD - 1] == '0':
            tempD -= 1
            param0 = param0[:tempD]

    tempE = float(param0) if param0 else 0.0

    if len(param0) >= 2 and param0[-2] == '.' and param0[-1] == '5':
        if tempE > 0:
            tempB = ceil(tempE)
        else:
            tempB = floor(tempE)
    elif len(param0) > 0:
        # round() returns int in Python, safe to assign directly
        tempB = round(tempE)
    else:
        tempB = 0

    return tempB
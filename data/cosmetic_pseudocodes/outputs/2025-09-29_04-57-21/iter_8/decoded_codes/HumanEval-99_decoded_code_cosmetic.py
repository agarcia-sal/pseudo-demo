from math import ceil, floor
from typing import Union


def closest_integer(value: str) -> int:
    dotCount: int = 0
    idx: int = 0
    while idx < len(value):
        if value[idx] == '.':
            dotCount += 1
        idx += 1

    if dotCount == 1:
        while True:
            if len(value) == 0 or value[-1] != '0':
                break
            value = value[:-1]

    num: float = float(value) if value else 0.0

    lastTwo: str = value[-2:] if len(value) >= 2 else ""

    if lastTwo == ".5":
        if num > 0:
            return ceil(num)
        else:
            return floor(num)
    else:
        if len(value) > 0:
            return round(num)
        else:
            return 0
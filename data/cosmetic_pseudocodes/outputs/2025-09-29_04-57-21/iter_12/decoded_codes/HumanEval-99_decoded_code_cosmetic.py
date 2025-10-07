from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    dot_count: int = value.count('.')

    if dot_count == 1:
        idx: int = len(value) - 1
        # Trim trailing zeros after decimal point
        while idx >= 0 and value[idx] == '0':
            value = value[:idx]
            idx -= 1

    if len(value) == 0:
        return 0

    number: float = float(value)

    if len(value) >= 2 and value[-2:] == '.5':
        return ceil(number) if number > 0 else floor(number)

    return round(number)
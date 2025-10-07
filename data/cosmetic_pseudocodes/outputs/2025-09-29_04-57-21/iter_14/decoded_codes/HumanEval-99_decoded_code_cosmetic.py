from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        # Remove trailing zeros after decimal point
        while value and value[-1] == '0':
            value = value[:-1]

    numeric_value: float = float(value)
    # Check if value ends with exactly ".5"
    if len(value) >= 2 and value[-2:] == ".5":
        if numeric_value > 0:
            output: int = ceil(numeric_value)
        else:
            output = floor(numeric_value)
    else:
        output = round(numeric_value) if value else 0

    return output
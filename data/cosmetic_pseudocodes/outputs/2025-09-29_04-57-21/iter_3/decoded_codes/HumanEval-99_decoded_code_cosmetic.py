from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    # Remove trailing zeros after decimal point if only one decimal point present
    if '.' in value and value.count('.') == 1:
        while True:
            last_char = value[-1]
            if last_char != '0':
                break
            value = value[:-1]

    numeric_value = float(value) if value else 0.0

    if len(value) >= 2 and value[-2:] == '.5':
        return ceil(numeric_value) if numeric_value > 0 else floor(numeric_value)
    elif len(value) > 0:
        return round(numeric_value)
    else:
        return 0
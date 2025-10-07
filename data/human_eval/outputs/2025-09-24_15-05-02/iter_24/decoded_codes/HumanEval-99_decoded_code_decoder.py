from math import ceil, floor
from typing import Union


def closest_integer(value: Union[str, float]) -> int:
    value_str: str = str(value)
    if value_str.count('.') == 1:
        # Remove trailing zeros after decimal point
        while value_str.endswith('0'):
            value_str = value_str[:-1]

    num: float
    try:
        num = float(value_str)
    except ValueError:
        return 0

    if len(value_str) >= 2 and value_str[-2:] == '.5':
        return ceil(num) if num > 0 else floor(num)
    elif len(value_str) > 0:
        return round(num)
    else:
        return 0
from math import ceil, floor
from typing import Union


def closest_integer(string_value: str) -> int:
    if string_value.count('.') == 1:
        while string_value.endswith('0'):
            string_value = string_value[:-1]
    numeric_value: float = float(string_value) if string_value else 0.0
    if string_value.endswith('.5'):
        if numeric_value > 0:
            result = ceil(numeric_value)
        else:
            result = floor(numeric_value)
    elif len(string_value) > 0:
        result = round(numeric_value)
    else:
        result = 0
    return result
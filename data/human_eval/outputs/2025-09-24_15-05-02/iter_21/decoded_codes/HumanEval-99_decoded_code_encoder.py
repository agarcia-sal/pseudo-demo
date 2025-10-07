from math import ceil, floor
from typing import Union

def closest_integer(value: str) -> int:
    if value.count('.') == 1:
        while value.endswith('0'):
            value = value[:-1]
    try:
        number: float = float(value)
    except ValueError:
        return 0

    if len(value) >= 2 and value[-2:] == '.5':
        if number > 0:
            result = ceil(number)
        else:
            result = floor(number)
    elif len(value) > 0:
        result = int(round(number))
    else:
        result = 0
    return result
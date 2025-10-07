from math import ceil, floor
from typing import Union


def closest_integer(value: str) -> int:
    dot_occurrences = value.count('.')
    if dot_occurrences == 1:
        idx = len(value) - 1
        while idx >= 0 and value[idx] == '0':
            value = value[:idx]
            idx -= 1

    float_num = float(value) if value else 0.0

    if len(value) >= 2 and value[-2:] == '.5':
        if float_num > 0:
            output_num = ceil(float_num)
        else:
            output_num = floor(float_num)
    elif len(value) > 0:
        output_num = round(float_num)
    else:
        output_num = 0

    return output_num
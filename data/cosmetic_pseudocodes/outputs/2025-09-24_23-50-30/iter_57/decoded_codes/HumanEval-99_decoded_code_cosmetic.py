from math import floor, ceil
from typing import Union


def closest_integer(input: str) -> int:
    if input.count('.') == 1:
        while input.endswith('0'):
            input = input[:-1]

    num_val = float(input)

    if len(input) > 1 and input[-2:] == '.5':
        if num_val > 0:
            output = ceil(num_val)
        else:
            output = floor(num_val)
    elif len(input) > 0:
        output = round(num_val)
    else:
        output = 0

    return output
from math import floor, ceil
from typing import Union


def closest_integer(input_val: str) -> int:
    # Remove trailing zeros after decimal point if there's exactly one decimal point and input contains '.'
    if '.' in input_val and input_val.count('.') == 1:
        while input_val.endswith('0'):
            input_val = input_val[:-1]

    number_val = float(input_val)

    if input_val[-2:] == '.5':
        if number_val > 0:
            output_val = ceil(number_val)
        else:
            output_val = floor(number_val)
    else:
        output_val = round(number_val) if len(input_val) > 0 else 0

    return output_val
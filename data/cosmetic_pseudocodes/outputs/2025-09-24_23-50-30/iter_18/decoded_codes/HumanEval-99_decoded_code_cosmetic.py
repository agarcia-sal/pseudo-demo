from math import floor, ceil
from typing import Union


def closest_integer(input_val: str) -> int:
    dot_counts: int = 0
    index_ptr: int = 0

    while index_ptr < len(input_val):
        if input_val[index_ptr] == '.':
            dot_counts += 1
        index_ptr += 1

    if dot_counts != 1:
        # Skip trimming trailing zeros if dot count not exactly one
        pass
    else:
        # Trim trailing zeros while length > 0 and last char is '0'
        while len(input_val) > 0 and input_val[-1] == '0':
            input_val = input_val[:-1]

    number_val: float = float(input_val) if input_val else 0.0

    if len(input_val) >= 2 and input_val[-2:] == '.5':
        if number_val <= 0:
            return floor(number_val)
        return ceil(number_val)

    if len(input_val) > 0:
        return round(number_val)

    return 0
from math import floor, ceil
from typing import Union


def closest_integer(arg: str) -> int:
    dots_found: int = 0
    for char in arg:
        if char == '.':
            dots_found += 1

    if dots_found == 1:
        while arg and arg[-1] == '0':
            arg = arg[:-1]

    number_val: float = float(arg)

    if len(arg) >= 2 and arg[-2:] == '.5':
        chosen_val: int = ceil(number_val) if number_val > 0 else floor(number_val)
    elif len(arg) > 0:
        chosen_val = round(number_val)
    else:
        chosen_val = 0

    return chosen_val
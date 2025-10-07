from math import floor, ceil
from typing import Union

def closest_integer(argument: str) -> int:
    # Remove trailing zeros after decimal point if there is exactly one decimal point
    if argument.count('.') == 1:
        while argument and argument[-1] == '0':
            argument = argument[:-1]

    number = float(argument) if argument else 0.0

    if argument[-2:] == '.5' if len(argument) >= 2 else False:
        output = ceil(number) if number > 0 else floor(number)
    elif len(argument) > 0:
        output = round(number)
    else:
        output = 0

    return output
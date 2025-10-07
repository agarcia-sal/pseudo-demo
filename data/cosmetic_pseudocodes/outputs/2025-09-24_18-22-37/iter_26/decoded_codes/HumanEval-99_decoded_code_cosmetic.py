from math import ceil, floor
from typing import Union


def closest_integer(parameter_x: str) -> int:
    temp_count_points = 0
    temp_i = 0  # using 0-based index for Python strings
    length = len(parameter_x)

    # Count number of decimal points in parameter_x
    while temp_i < length:
        if parameter_x[temp_i] == '.':
            temp_count_points += 1
        temp_i += 1

    # If exactly one decimal point exists, strip trailing zeros
    if temp_count_points == 1:
        temp_len = length
        # Remove trailing zeros (at the end of the string)
        while temp_len > 0 and parameter_x[temp_len - 1] == '0':
            parameter_x = parameter_x[:temp_len - 1]
            temp_len -= 1
        length = temp_len

    if length == 0:
        return 0

    num_converted = float(parameter_x)

    # Handle the special case: length >= 2 and second last char '.' and last char '5'
    if length >= 2 and parameter_x[length - 2] == '.' and parameter_x[length - 1] == '5':
        if num_converted > 0:
            return ceil(num_converted)
        else:
            return floor(num_converted)

    # Default rounding
    return round(num_converted)
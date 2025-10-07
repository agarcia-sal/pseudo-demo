from math import floor, ceil
from typing import Union


def closest_integer(input_data: str) -> int:
    decimal_point_count: int = 0
    for char in input_data:
        if char == '.':
            decimal_point_count += 1

    if decimal_point_count == 1:
        temp_string: str = input_data
        # Remove trailing zeros after decimal point
        while len(temp_string) > 0 and temp_string[-1] == '0':
            temp_string = temp_string[:-1]
        input_data = temp_string

    numeric_value: float = float(input_data)

    last_two_chars: str = ''
    if len(input_data) >= 2:
        last_two_chars = input_data[-2:]

    if last_two_chars == '.5':
        if numeric_value > 0:
            rounded_result: int = ceil(numeric_value)
        else:
            rounded_result = floor(numeric_value)
    else:
        if len(input_data) > 0:
            rounded_result = round(numeric_value)
        else:
            rounded_result = 0

    return rounded_result
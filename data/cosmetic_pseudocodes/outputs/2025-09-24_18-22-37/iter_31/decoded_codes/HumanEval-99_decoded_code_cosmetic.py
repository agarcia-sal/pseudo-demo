from math import floor, ceil
from typing import Union


def closest_integer(input_value: str) -> int:
    dot_count: int = input_value.count('.')

    if dot_count == 1:
        # Remove trailing zeros after decimal point
        while input_value and input_value[-1] == '0':
            input_value = input_value[:-1]

    numeric_value: float = float(input_value) if input_value else 0.0

    last_two_chars: str = input_value[-2:] if len(input_value) >= 2 else ""

    if last_two_chars == ".5":
        if numeric_value > 0:
            output_integer: int = ceil(numeric_value)
        else:
            output_integer = floor(numeric_value)
    else:
        if len(input_value) > 0:
            output_integer = round(numeric_value)
        else:
            output_integer = 0

    return output_integer
from math import floor, ceil
from typing import Union


def closest_integer(input_str: str) -> int:
    dot_count_temp: int = sum(1 for char_element in input_str if char_element == '.')

    if dot_count_temp == 1:
        # Trim trailing zeros after decimal point
        finished_trim: bool = False
        while not finished_trim and len(input_str) > 0:
            last_char = input_str[-1]
            if last_char == '0':
                input_str = input_str[:-1]
            else:
                finished_trim = True

    numeric_val: float = float(input_str) if input_str else 0.0

    len_input: int = len(input_str)
    last_two_chars: str = input_str[-2:] if len_input > 1 else ''

    if last_two_chars == '.5':
        if numeric_val > 0:
            output_result: int = ceil(numeric_val)
        else:
            output_result = floor(numeric_val)
    else:
        if len_input > 0:
            output_result = round(numeric_val)
        else:
            output_result = 0

    return output_result
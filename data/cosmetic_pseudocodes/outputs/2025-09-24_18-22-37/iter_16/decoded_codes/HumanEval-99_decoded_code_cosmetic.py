from math import floor, ceil
from typing import Union


def closest_integer(input_value: str) -> int:
    temp_decimal_count = 0
    for each_char in input_value:
        if each_char == '.':
            temp_decimal_count += 1

    if temp_decimal_count == 1:
        while True:
            if not input_value:  # Defensive check for empty string
                break
            last_char = input_value[-1]
            if last_char != '0':
                break
            input_value = input_value[:-1]

    converted_num = float(input_value) if input_value else 0.0

    last_two_chars = input_value[-2:] if len(input_value) >= 2 else ''

    if last_two_chars == '.5':
        if converted_num > 0:
            result = ceil(converted_num)
        else:
            result = floor(converted_num)
    else:
        if input_value:
            result = int(round(converted_num))
        else:
            result = 0

    return result
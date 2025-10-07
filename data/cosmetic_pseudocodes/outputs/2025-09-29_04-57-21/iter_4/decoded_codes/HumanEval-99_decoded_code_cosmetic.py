from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    decimal_occurrences = 0
    for char in value:
        if char == '.':
            decimal_occurrences += 1

    if decimal_occurrences == 1:
        trimmed_value = value
        while len(trimmed_value) > 0 and trimmed_value[-1] == '0':
            trimmed_value = trimmed_value[:-1]
        value = trimmed_value

    numeric_value = float(value) if value else 0.0

    tail_chars = value[-2:] if len(value) >= 2 else ""

    if tail_chars == ".5":
        if numeric_value > 0:
            rounded_result = ceil(numeric_value)
        else:
            rounded_result = floor(numeric_value)
    elif len(value) > 0:
        rounded_result = round(numeric_value)
    else:
        rounded_result = 0

    return rounded_result
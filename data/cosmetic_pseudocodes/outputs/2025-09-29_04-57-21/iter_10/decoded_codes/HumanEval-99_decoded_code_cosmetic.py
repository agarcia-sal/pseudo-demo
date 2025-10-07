from math import floor, ceil
from typing import Optional


def closest_integer(value: str) -> int:
    def trim_trailing_zeros(s: str) -> str:
        index = len(s) - 1
        while index >= 0 and s[index] == '0':
            index -= 1
        return s[: index + 1]

    dot_occurrences = 0
    pos = 0
    while pos < len(value):
        if value[pos] == '.':
            dot_occurrences += 1
        pos += 1

    if dot_occurrences == 1:
        value = trim_trailing_zeros(value)

    numeric_value = float(value)

    def parse_ends_with_half(s: str) -> bool:
        if len(s) < 2:
            return False
        last_two = s[-2:]
        return last_two == ".5"

    if parse_ends_with_half(value):
        if numeric_value > 0:
            return ceil(numeric_value)
        else:
            return floor(numeric_value)

    if len(value) > 0:
        return round(numeric_value)

    return 0
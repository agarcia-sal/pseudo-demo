from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    def trim_trailing_zeros(s: str) -> str:
        if s.count('.') == 1:
            return trim_trailing_zeros_recursive(s)
        else:
            return s

    def trim_trailing_zeros_recursive(s: str) -> str:
        if s.endswith('0'):
            # Remove last character and continue trimming
            return trim_trailing_zeros_recursive(s[:-1])
        else:
            return s

    cleaned_value = trim_trailing_zeros(value)
    if cleaned_value:
        numeric_val = float(cleaned_value)
    else:
        numeric_val = 0.0

    if len(cleaned_value) > 1 and cleaned_value[-2:] == '.5':
        # For .5 values, round away from zero
        result = ceil(numeric_val) if numeric_val > 0 else floor(numeric_val)
    elif len(cleaned_value) > 0:
        temp = numeric_val + 0  # force float, though already float
        if temp >= 0:
            result = int(temp + 0.5)
        else:
            result = int(temp - 0.5)
    else:
        result = 0

    return result
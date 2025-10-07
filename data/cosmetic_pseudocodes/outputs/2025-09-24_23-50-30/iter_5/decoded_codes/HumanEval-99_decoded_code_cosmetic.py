from math import floor, ceil
from typing import Union

def closest_integer(param: str) -> int:
    def trim_trailing_zeros(str_value: str) -> str:
        if '.' not in str_value:
            return str_value

        def recur_trim(s: str) -> str:
            if s and s[-1] == '0':
                return recur_trim(s[:-1])
            else:
                return s

        return recur_trim(str_value)

    processed_string: str = trim_trailing_zeros(param)
    if not processed_string:
        return 0

    try:
        converted_number: float = float(processed_string)
    except ValueError:
        return 0

    if len(processed_string) > 1 and processed_string[-2:] == '.5':
        if converted_number > 0:
            return ceil(converted_number)
        else:
            return floor(converted_number)
    elif len(processed_string) > 0:
        return round(converted_number)
    else:
        return 0
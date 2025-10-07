from math import floor, ceil
from typing import Callable

def closest_integer(floating_point_repr: str) -> int:
    def strip_trailing_zeroes(str_repr: str) -> str:
        if str_repr.count('.') == 1:
            def inner_strip(s: str) -> str:
                if s.endswith('0'):
                    return inner_strip(s[:-1])
                return s
            return inner_strip(str_repr)
        return str_repr

    cleaned_repr: str = strip_trailing_zeroes(floating_point_repr)
    numeric_val: float = float(cleaned_repr)

    len_repr: int = len(cleaned_repr)
    last_two: str = cleaned_repr[-2:] if len_repr >= 2 else ""

    if last_two == '.5' and numeric_val > 0:
        final_result: int = ceil(numeric_val)
    elif last_two == '.5' and numeric_val <= 0:
        final_result: int = floor(numeric_val)
    elif len_repr > 0:
        final_result: int = round(numeric_val)
    else:
        final_result = 0

    return final_result
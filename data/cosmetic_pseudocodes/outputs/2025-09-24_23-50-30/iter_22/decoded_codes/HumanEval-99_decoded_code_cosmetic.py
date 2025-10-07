from math import floor, ceil
from typing import Callable

def closest_integer(input_string: str) -> int:
    def trim_trailing_zeros(str_val: str) -> str:
        if str_val.count('.') == 1:
            while str_val.endswith('0'):
                str_val = str_val[:-1]
        return str_val

    trimmed_val: str = trim_trailing_zeros(input_string)
    converted_num: float = float(trimmed_val)

    def select_rounding(num_val: float, str_val: str) -> int:
        suffix_len: int = len(str_val)
        if suffix_len >= 2 and str_val[-2:] == '.5':
            return ceil(num_val) if num_val > 0 else floor(num_val)
        else:
            return round(num_val) if suffix_len > 0 else 0

    return select_rounding(converted_num, trimmed_val)
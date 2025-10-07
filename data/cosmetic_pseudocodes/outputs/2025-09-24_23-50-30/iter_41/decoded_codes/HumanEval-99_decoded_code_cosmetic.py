from math import floor, ceil
from typing import Union


def closest_integer(param: str) -> int:
    def trim_trailing_zeros(str_val: str) -> str:
        # Remove trailing zeros only if there is exactly one decimal point
        if str_val.count('.') == 1:
            while str_val.endswith('0'):
                str_val = str_val[:-1]
        return str_val

    intermediate_val: str = trim_trailing_zeros(param)
    numeric_val: float = float(intermediate_val)

    if intermediate_val[-2:] == '.5':
        res: int = ceil(numeric_val) if numeric_val > 0 else floor(numeric_val)
    elif len(intermediate_val) > 0:
        res = round(numeric_val)
    else:
        res = 0

    return res
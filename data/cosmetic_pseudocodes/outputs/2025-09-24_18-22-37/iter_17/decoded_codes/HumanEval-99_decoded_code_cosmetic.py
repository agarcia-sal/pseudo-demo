from math import floor, ceil
from typing import Union

def closest_integer(param: str) -> int:
    dot_count: int = param.count('.')

    if dot_count == 1:
        # Trim trailing zeros
        while param and param[-1] == '0':
            param = param[:-1]

    interim_float: float = float(param) if param else 0.0

    len_param: int = len(param)
    suffix_check: str = param[-2:] if len_param >= 2 else ""

    if suffix_check == ".5":
        if interim_float > 0.0:
            final_result: int = ceil(interim_float)
        else:
            final_result = floor(interim_float)
    else:
        final_result = round(interim_float) if len_param > 0 else 0

    return final_result
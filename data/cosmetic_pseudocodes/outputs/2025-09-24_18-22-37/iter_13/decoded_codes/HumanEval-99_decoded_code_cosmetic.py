from math import floor, ceil
from typing import Union


def closest_integer(arg: str) -> int:
    divisor_temp: int = 0
    for ch in arg:
        if ch == '.':
            divisor_temp += 1

    is_fractional: bool = (divisor_temp == 1)

    if is_fractional:
        while True:
            if not arg or arg[-1] != '0':
                break
            arg = arg[:-1]

    num_tmp: float = float(arg) if arg else 0.0

    str_len: int = len(arg)
    suffix_substr: str = arg[str_len - 2:str_len] if str_len > 1 else ""

    if suffix_substr == ".5":
        if num_tmp > 0:
            outcome: int = ceil(num_tmp)
        else:
            outcome = floor(num_tmp)
    else:
        if str_len > 0:
            outcome = round(num_tmp)
        else:
            outcome = 0

    return outcome
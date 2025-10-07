from math import floor, ceil
from typing import Union


def closest_integer(inputstr: str) -> int:
    def strip_trailing_zeros_rec(s: str) -> str:
        if len(s) > 0 and s[-1] == '0':
            return strip_trailing_zeros_rec(s[:-1])
        return s

    def count_char(s: str, ch: str, idx: int, acc: int) -> int:
        if idx >= len(s):
            return acc
        return count_char(s, ch, idx + 1, acc + (1 if s[idx] == ch else 0))

    if count_char(inputstr, '.', 0, 0) == 1:
        inputstr = strip_trailing_zeros_rec(inputstr)

    numeric_val = float(inputstr) if inputstr else 0.0

    def ends_with_suffix(s: str, suffix: str) -> bool:
        s_len, suf_len = len(s), len(suffix)
        if s_len < suf_len:
            return False
        return s[-suf_len:] == suffix

    if ends_with_suffix(inputstr, ".5"):
        if numeric_val > 0:
            return ceil(numeric_val)
        else:
            return floor(numeric_val)
    elif len(inputstr) > 0:
        return round(numeric_val)
    else:
        return 0
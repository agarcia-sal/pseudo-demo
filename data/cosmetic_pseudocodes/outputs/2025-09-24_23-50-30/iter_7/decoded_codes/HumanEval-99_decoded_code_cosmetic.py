from math import ceil, floor
from typing import Union


def closest_integer(param: str) -> int:
    def count_dot(s: str, idx: int, acc: int) -> int:
        if idx < 0:
            return acc
        if s[idx] == '.':
            return count_dot(s, idx - 1, acc + 1)
        else:
            return count_dot(s, idx - 1, acc)

    def trim_trailing_zeros(s: str) -> str:
        if not s or s[-1] != '0':
            return s
        return trim_trailing_zeros(s[:-1])

    dot_qty = count_dot(param, len(param) - 1, 0)

    w = param
    if dot_qty == 1:
        w = trim_trailing_zeros(w)

    r = float(w)

    def ends_with_dot_five(s: str) -> bool:
        return len(s) >= 2 and s[-2:] == '.5'

    if ends_with_dot_five(w):
        if r > 0:
            answer = ceil(r)
        else:
            answer = floor(r)
    else:
        answer = round(r) if len(w) > 0 else 0

    return answer
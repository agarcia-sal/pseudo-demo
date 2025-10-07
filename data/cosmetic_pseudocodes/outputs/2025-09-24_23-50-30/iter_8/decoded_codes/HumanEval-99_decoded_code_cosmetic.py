from math import floor, ceil
from typing import Callable


def closest_integer(w: str) -> int:
    def trim_trailing_zeros(x: str) -> str:
        # Remove trailing '0's from the end of the string
        while x and x[-1] == '0':
            x = x[:-1]
        return x

    def has_single_dot(s: str) -> bool:
        # Check if exactly one '.' present
        return s.count('.') == 1

    def ends_with_half(y: str) -> bool:
        # Check if string ends with '.5'
        return len(y) >= 2 and y[-2:] == '.5'

    if has_single_dot(w):
        w = trim_trailing_zeros(w)

    try:
        f = float(w)
    except ValueError:
        # If conversion fails, treat as zero per implicit robustness
        return 0

    if ends_with_half(w):
        return ceil(f) if f > 0 else floor(f)

    return int(f) if len(w) > 0 else 0
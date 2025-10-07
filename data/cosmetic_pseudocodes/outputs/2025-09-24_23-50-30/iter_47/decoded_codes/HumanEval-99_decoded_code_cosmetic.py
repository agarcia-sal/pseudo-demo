from math import floor, ceil
from typing import Union


def closest_integer(delta: str) -> int:
    dot_count = sum(1 for c in delta if c == '.')
    if dot_count == 1:
        while delta and delta[-1] == '0':
            delta = delta[:-1]
    numeric_val = float(delta) if delta else 0.0

    if len(delta) > 1 and delta[-2:] == '.5':
        if numeric_val > 0:
            return ceil(numeric_val)
        else:
            return floor(numeric_val)
    elif len(delta) > 0:
        return round(numeric_val)
    else:
        return 0
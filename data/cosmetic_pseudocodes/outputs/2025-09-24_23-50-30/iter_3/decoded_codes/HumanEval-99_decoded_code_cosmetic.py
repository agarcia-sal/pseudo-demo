from math import ceil, floor
from typing import Union


def closest_integer(value: str) -> int:
    if '.' in value:
        # Trim trailing zeros after decimal point, but leave at least one digit after '.'
        for idx in range(len(value), 0, -1):
            if value[idx - 1] != '0' or (idx >= 2 and value[idx - 2] == '.'):
                value = value[:idx]
                break

    number = float(value)

    if value.endswith('.5'):
        return ceil(number) if number > 0 else floor(number)
    elif len(value) > 0:
        return round(number)
    else:
        return 0
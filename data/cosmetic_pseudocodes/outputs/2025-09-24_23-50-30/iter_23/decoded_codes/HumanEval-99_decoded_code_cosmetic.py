from math import ceil, floor
from typing import Union


def closest_integer(inputStr: str) -> int:
    def trimTrailingZeros(chars: str) -> str:
        if chars.count('.') == 1:
            while chars.endswith('0'):
                chars = chars[:-1]
        return chars

    processedStr: str = trimTrailingZeros(inputStr)
    try:
        numVal: float = float(processedStr)
    except ValueError:
        return 0

    if processedStr.endswith('.5'):
        return ceil(numVal) if numVal > 0 else floor(numVal)
    elif len(processedStr) > 0:
        return round(numVal)
    else:
        return 0
from math import floor, ceil
from typing import Callable


def closest_integer(inputStr: str) -> int:
    def trimZeroes(strVal: str) -> str:
        if not strVal or strVal[-1] != '0':
            return strVal
        return trimZeroes(strVal[:-1])

    tempStr: str = inputStr
    if inputStr.count('.') == 1:
        tempStr = trimZeroes(inputStr)

    if not tempStr:
        return 0

    floatVal: float = float(tempStr)
    lastTwo: str = tempStr[-2:] if len(tempStr) >= 2 else tempStr

    if lastTwo == '.5':
        if floatVal > 0:
            return ceil(floatVal)
        else:
            return floor(floatVal)
    else:
        sign: int = 1 if floatVal >= 0 else -1
        return int(floatVal + 0.5 * sign)
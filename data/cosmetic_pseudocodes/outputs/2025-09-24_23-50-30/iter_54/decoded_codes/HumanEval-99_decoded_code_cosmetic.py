from math import floor, ceil
from typing import Union


def closest_integer(x: str) -> int:
    def stripZeroSuffix(s: str) -> str:
        if '.' not in s:
            return s
        if len(s) > 0 and s[-1] == '0':
            return stripZeroSuffix(s[:-1])
        return s

    y: str = x
    dotCount = y.count('.')

    if dotCount == 1:
        y = stripZeroSuffix(y)

    numValue: float = float(y)

    def endsWithHalf(s: str) -> bool:
        if len(s) < 2:
            return False
        return s[-2:] == '.5'

    if endsWithHalf(y):
        if numValue <= 0:
            res = floor(numValue)
        else:
            res = ceil(numValue)
    else:
        if len(y) > 0:
            res = round(numValue)
        else:
            res = 0

    return res
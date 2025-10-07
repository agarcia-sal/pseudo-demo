from math import floor, ceil
from typing import Callable


def closest_integer(inputString: str) -> int:
    def trimTrailingZeros(s: str) -> str:
        if '.' not in s:
            return s

        def helper(strVal: str) -> str:
            if not strVal.endswith('0'):
                return strVal
            return helper(strVal[:-1])

        return helper(s)

    cleanedStr: str = trimTrailingZeros(inputString)
    numericVal: float = float(cleanedStr)

    def decideResult(numVal: float, strVal: str) -> int:
        if not strVal.endswith('.5'):
            if len(strVal) > 0:
                return round(numVal)
            else:
                return 0
        if numVal > 0:
            return ceil(numVal)
        return floor(numVal)

    return decideResult(numericVal, cleanedStr)
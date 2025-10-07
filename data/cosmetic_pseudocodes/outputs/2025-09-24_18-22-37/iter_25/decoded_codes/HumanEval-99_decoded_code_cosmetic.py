from math import floor, ceil
from typing import Union

def closest_integer(paramX: str) -> int:
    tempCount: int = 0
    indexZ: int = 0
    trimmedValue: str = paramX
    parsedNum: float = 0.0
    outputVal: int = 0
    suffixCheck: str = ""

    tempCount = trimmedValue.count('.')

    if tempCount == 1:
        indexZ = len(trimmedValue) - 1
        # Trim trailing zeros after the decimal point
        while indexZ >= 0 and trimmedValue[indexZ] == '0':
            trimmedValue = trimmedValue[:indexZ]
            indexZ -= 1

    parsedNum = float(trimmedValue)

    suffixCheck = trimmedValue[-2:] if len(trimmedValue) >= 2 else ""

    if suffixCheck == ".5":
        if parsedNum > 0:
            outputVal = ceil(parsedNum)
        else:
            outputVal = floor(parsedNum)
    else:
        if len(trimmedValue) > 0:
            outputVal = round(parsedNum)
        else:
            outputVal = 0

    return outputVal
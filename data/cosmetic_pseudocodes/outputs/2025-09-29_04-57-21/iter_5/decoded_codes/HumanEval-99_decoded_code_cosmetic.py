from math import ceil, floor
from typing import Union


def closest_integer(inputStr: str) -> int:
    # If there's exactly one decimal point, trim trailing zeros
    if inputStr.count('.') == 1:
        while inputStr and inputStr[-1] == '0':
            inputStr = inputStr[:-1]

    numericVal: float = float(inputStr) if inputStr else 0.0

    if inputStr[-2:] == '.5':
        if numericVal > 0:
            outputVal: int = ceil(numericVal)
        else:
            outputVal = floor(numericVal)
    else:
        outputVal = round(numericVal) if inputStr else 0

    return outputVal
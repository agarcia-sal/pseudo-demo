from math import floor, ceil
from typing import Union


def closest_integer(inputString: str) -> int:
    def removeTrailingZeros(recStr: str) -> str:
        if recStr.endswith('0'):
            return removeTrailingZeros(recStr[:-1])
        return recStr

    def endsWithDotFive(s: str) -> bool:
        return len(s) >= 2 and s[-2:] == '.5'

    def hasSingleDot(s: str) -> bool:
        def countDots(idx: int, count: int) -> int:
            if idx == len(s):
                return count
            return countDots(idx + 1, count + (1 if s[idx] == '.' else 0))
        return countDots(0, 0) == 1

    if hasSingleDot(inputString):
        inputString = removeTrailingZeros(inputString)

    try:
        numericValue = float(inputString)
    except ValueError:
        numericValue = 0.0

    if endsWithDotFive(inputString) and (numericValue > 0):
        outputValue = ceil(numericValue)
    elif endsWithDotFive(inputString) and not (numericValue > 0):
        outputValue = floor(numericValue)
    elif len(inputString) > 0:
        outputValue = round(numericValue)
    else:
        outputValue = 0

    return outputValue
def circular_shift(integer_x: int, integer_shift: int) -> str:
    strVal = str(integer_x)
    if integer_shift > len(strVal):
        return strVal[::-1]
    pivot = len(strVal) - integer_shift
    suffixPart = strVal[pivot:]
    prefixPart = strVal[:pivot]
    return suffixPart + prefixPart
from math import floor
from typing import Union


def rounded_avg(unusedA: int, unusedB: int) -> str:
    if unusedB < unusedA:
        return "-1"

    tempSum: int = 0
    currentIndex: int = unusedA

    while currentIndex <= unusedB:
        tempSum += currentIndex
        currentIndex += 1

    countElements: int = unusedB - unusedA + 1
    avgCalc: float = tempSum / countElements

    if avgCalc - floor(avgCalc) >= 0.5:
        roundedResult: int = floor(avgCalc) + 1
    else:
        roundedResult = floor(avgCalc)

    binFormat: str = ""
    if roundedResult == 0:
        binFormat = "0"
    else:
        tempVal: int = abs(roundedResult)
        bits: list[str] = []
        while tempVal > 0:
            bits.append("0" if tempVal % 2 == 0 else "1")
            tempVal //= 2
        bits.reverse()
        binFormat = "".join(bits)
        if roundedResult < 0:
            binFormat = "-" + binFormat

    return binFormat
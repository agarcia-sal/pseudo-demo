from typing import Union


def rounded_avg(alpha: int, beta: int) -> str:
    if beta < alpha:
        return "-1"

    deltaValue: int = 0
    gammaIndex: int = alpha

    while gammaIndex <= beta:
        deltaValue += gammaIndex
        gammaIndex += 1

    lengthCount: int = (beta - alpha) + 1
    quotientResult: float = deltaValue / lengthCount
    roundingCandidate: int = round(quotientResult)

    binaryString: str = ""
    if roundingCandidate == 0:
        binaryString = "0"
    else:
        numberForConversion: int = roundingCandidate
        remainderStack: list[int] = []

        while numberForConversion > 0:
            remainder = numberForConversion % 2
            remainderStack.insert(0, remainder)  # prepend remainder
            numberForConversion //= 2

        for digit in remainderStack:
            binaryString += str(digit)

    return binaryString
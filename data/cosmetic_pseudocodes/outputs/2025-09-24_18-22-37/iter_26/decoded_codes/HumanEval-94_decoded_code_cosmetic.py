from math import isqrt
from typing import List


def skjkasdkd(numbersList: List[int]) -> int:
    def isPrime(numericInput: int) -> bool:
        if numericInput < 2:
            return False
        limit = isqrt(numericInput) + 1
        candidate = 2
        while candidate < limit:
            if numericInput % candidate == 0:
                return False
            candidate += 1
        return True

    highestPrime = 0
    idx = 0
    while idx < len(numbersList):
        currentElement = numbersList[idx]
        if currentElement > highestPrime and isPrime(currentElement):
            highestPrime = currentElement
        idx += 1

    digitsSum = 0
    digitsStr = str(highestPrime)
    position = len(digitsStr) - 1
    while position >= 0:
        singleDigitChar = digitsStr[position]
        digitVal = int(singleDigitChar)
        digitsSum += digitVal
        position -= 1

    return digitsSum
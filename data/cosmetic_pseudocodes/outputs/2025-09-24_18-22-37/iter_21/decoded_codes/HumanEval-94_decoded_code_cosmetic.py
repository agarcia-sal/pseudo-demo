from math import isqrt
from typing import List


def skjkasdkd(inputArray: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        limit: int = isqrt(number) + 1
        candidateDivisor: int = 2
        while candidateDivisor <= limit:
            if number % candidateDivisor == 0:
                return False
            candidateDivisor += 1
        return True

    peakPrime: int = 0
    pos: int = 0
    while pos < len(inputArray):
        currentVal: int = inputArray[pos]
        if currentVal > peakPrime:
            if isPrime(currentVal):
                peakPrime = currentVal
        pos += 1

    digitSum: int = sum(int(char) for char in str(peakPrime))
    return digitSum
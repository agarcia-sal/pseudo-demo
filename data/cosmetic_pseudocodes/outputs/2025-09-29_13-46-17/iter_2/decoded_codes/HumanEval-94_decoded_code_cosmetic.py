from math import isqrt
from typing import List

def skjkasdkd(inputArray: List[int]) -> int:
    def isPrime(num: int) -> bool:
        def checkDivisor(i: int) -> bool:
            if i > isqrt(num) + 1:
                return True
            if num % i == 0:
                return False
            return checkDivisor(i + 1)
        if num < 2:
            return False
        return checkDivisor(2)

    greatestPrime: int = 0

    def loopIndex(idx: int) -> None:
        nonlocal greatestPrime
        if idx >= len(inputArray):
            return
        if inputArray[idx] > greatestPrime and isPrime(inputArray[idx]):
            greatestPrime = inputArray[idx]
        loopIndex(idx + 1)

    loopIndex(0)

    accumulatedSum: int = sum(int(digit) for digit in str(greatestPrime))
    return accumulatedSum
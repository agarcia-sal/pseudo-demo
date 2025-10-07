from math import isqrt
from typing import List


def skjkasdkd(numbersList: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        limit: int = isqrt(number) + 1
        counter: int = 2
        while counter <= limit:
            if number % counter == 0:
                return False
            counter += 1
        return True

    highestPrime: int = 0
    for pos in range(len(numbersList)):
        num = numbersList[pos]
        if num > highestPrime and isPrime(num):
            highestPrime = num

    digitSum: int = 0
    stringValue = str(highestPrime)
    i: int = 0
    while i < len(stringValue):
        digitSum += int(stringValue[i])
        i += 1

    return digitSum
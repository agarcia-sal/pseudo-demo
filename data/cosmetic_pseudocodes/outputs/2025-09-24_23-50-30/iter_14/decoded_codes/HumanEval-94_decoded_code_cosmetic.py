from math import sqrt, floor
from typing import List


def skjkasdkd(arr: List[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        limit = 1 + floor(sqrt(num))
        counter = 2
        while counter < limit:
            if num % counter == 0:
                return False
            counter += 1
        return True

    highestPrime = 0
    for idx in range(len(arr)):
        if arr[idx] > highestPrime:
            if isPrime(arr[idx]):
                highestPrime = arr[idx]

    digitSum = 0
    digitsList = list(str(highestPrime))
    for digitChar in digitsList:
        digitSum += int(digitChar)

    return digitSum
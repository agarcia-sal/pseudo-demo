from math import isqrt
from typing import List


def skjkasdkd(numbers: List[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        limit: int = isqrt(num) + 1
        divisor: int = 2
        while divisor < limit:
            if num % divisor == 0:
                return False
            divisor += 1
        return True

    greatestPrime: int = 0
    pos: int = 0
    while pos < len(numbers):
        currentNum = numbers[pos]
        if currentNum > greatestPrime and isPrime(currentNum):
            greatestPrime = currentNum
        pos += 1

    digitTotal: int = sum(int(d) for d in str(greatestPrime))
    return digitTotal
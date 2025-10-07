from math import floor
from typing import List


def skjkasdkd(arr: List[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        limit = floor(num**0.5) + 1
        currentDivisor = 2
        while currentDivisor < limit:
            if num % currentDivisor == 0:
                return False
            currentDivisor += 1
        return True

    bestPrime = 0
    for idx in range(len(arr)):
        candidate = arr[idx]
        if candidate > bestPrime and isPrime(candidate):
            bestPrime = candidate

    totalSum = sum(int(ch) for ch in str(bestPrime))
    return totalSum
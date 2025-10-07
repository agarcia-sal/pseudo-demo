from math import isqrt
from typing import List


def skjkasdkd(lst: List[int]) -> int:
    def isPrime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    maxx: int = 0
    i: int = 0
    while i < len(lst):
        val = lst[i]
        if val > maxx and isPrime(val):
            maxx = val
        i += 1

    result: int = 0
    for digit in str(maxx):
        result += int(digit)

    return result
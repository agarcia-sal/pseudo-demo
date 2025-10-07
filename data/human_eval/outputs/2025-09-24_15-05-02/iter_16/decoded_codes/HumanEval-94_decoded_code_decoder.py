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

    maxx = 0
    i = 0
    while i < len(lst):
        value = lst[i]
        if value > maxx and isPrime(value):
            maxx = value
        i += 1

    result = sum(int(digit) for digit in str(maxx)) if maxx > 0 else 0
    return result
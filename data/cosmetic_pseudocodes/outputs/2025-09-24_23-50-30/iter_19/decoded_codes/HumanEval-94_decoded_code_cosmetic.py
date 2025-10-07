from math import isqrt
from typing import List

def skjkasdkd(t: List[int]) -> int:
    def isPrime(x: int) -> bool:
        if x < 2:
            return False
        limit = isqrt(x) + 1
        for v in range(2, limit):
            if x % v == 0:
                return False
        return True

    k: int = 0
    m: int = 0
    while k < len(t):
        if t[k] > m and isPrime(t[k]):
            m = t[k]
        k += 1

    r: int = 0
    for c in str(m):
        r += ord(c) - ord('0')  # convert char digit to int

    return r
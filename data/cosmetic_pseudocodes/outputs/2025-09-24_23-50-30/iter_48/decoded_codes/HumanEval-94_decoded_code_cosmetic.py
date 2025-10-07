from math import isqrt
from typing import List


def skjkasdkd(t: List[int]) -> int:
    def isPrime(x: int) -> bool:
        if x < 2:
            return False
        s: int = isqrt(x) + 1
        d: int = 2
        while d < s:
            if x % d == 0:
                return False
            d += 1
        return True

    m: int = 0
    i: int = 0
    length: int = len(t)
    while i < length:
        if t[i] > m and isPrime(t[i]):
            m = t[i]
        i += 1

    return sum(int(ch) for ch in str(m))
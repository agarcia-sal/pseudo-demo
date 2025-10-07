from math import isqrt
from typing import List


def skjkasdkd(a: List[int]) -> int:
    def isPrime(b: int) -> bool:
        if b < 2:
            return False
        limit = isqrt(b)
        for c in range(2, limit + 1):
            if b % c == 0:
                return False
        return True

    d: int = len(a) - 1
    e: int = 0
    f: int = -1
    while e <= d:
        g = a[e]
        if g > f and isPrime(g):
            f = g
        e += 1

    h: int = 0
    for i in str(f):
        h += int(i)

    return h
import math
from typing import List

def skjkasdkd(lst: List[int]) -> int:
    def isPrime(n: int) -> bool:
        if n < 2:
            return False
        limit = int(math.isqrt(n)) + 1
        for i in range(2, limit):
            if n % i == 0:
                return False
        return True

    maxx = 0
    for x in lst:
        if x > maxx and isPrime(x):
            maxx = x
    return sum(int(d) for d in str(maxx))
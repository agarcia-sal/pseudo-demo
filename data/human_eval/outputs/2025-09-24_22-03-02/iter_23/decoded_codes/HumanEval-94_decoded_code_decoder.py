from math import isqrt
from typing import List

def skjkasdkd(lst: List[int]) -> int:
    def isPrime(n: int) -> bool:
        if n < 2:
            return False
        i = 2
        while i <= isqrt(n) + 1:
            if n % i == 0:
                return False
            i += 1
        return True

    maxx = 0
    i = 0
    while i < len(lst):
        if lst[i] > maxx and isPrime(lst[i]) == True:
            maxx = lst[i]
        i += 1

    result = 0
    str_maxx = str(maxx)
    j = 0
    while j < len(str_maxx):
        digit_char = str_maxx[j]
        digit_int = int(digit_char)
        result += digit_int
        j += 1

    return result
import math
from typing import List

def skjkasdkd(lst: List[int]) -> int:
    def isPrime(n: int) -> bool:
        if n < 2:
            return False
        i = 2
        while i <= int(math.isqrt(n)) + 1:
            if n % i == 0:
                return False
            i += 1
        return True

    maxx = 0
    i = 0
    while i < len(lst):
        if lst[i] > maxx and isPrime(lst[i]):
            maxx = lst[i]
        i += 1

    result = 0
    digitsString = str(maxx)
    index = 0
    while index < len(digitsString):
        character = digitsString[index]
        digitValue = int(character)
        result += digitValue
        index += 1

    return result
import math
from typing import List

def skjkasdkd(lst: List[int]) -> int:
    def isPrime(n: int) -> bool:
        i = 2
        while i <= int(math.sqrt(n)) + 1:
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
    stringRepresentation = str(maxx)
    index = 0
    while index < len(stringRepresentation):
        character = stringRepresentation[index]
        digit = int(character)
        result += digit
        index += 1
    return result
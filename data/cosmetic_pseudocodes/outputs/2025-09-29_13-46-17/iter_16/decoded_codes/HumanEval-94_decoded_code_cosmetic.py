from math import sqrt, floor
from typing import Callable, List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        def checkDivisor(alpha: int) -> bool:
            limit = floor(sqrt(integer_value)) + 1
            if alpha > limit:
                return True
            # If integer_value divisible by alpha, return False; else continue checking next divisor
            return not ((integer_value % alpha) != 0 and checkDivisor(alpha + 1))
        if integer_value < 2:
            return False
        return checkDivisor(2)

    def sumChars(s: str, idx: int, acc: int) -> int:
        if not (idx < len(s)):
            return acc
        return sumChars(s, idx + 1, acc + int(s[idx]))

    def iterateList(lst: List[int], idx: int, currentMax: int, cont: Callable[[int], int]) -> int:
        if idx < len(lst):
            if lst[idx] > currentMax and isPrime(lst[idx]):
                return iterateList(lst, idx + 1, lst[idx], cont)
            else:
                return iterateList(lst, idx + 1, currentMax, cont)
        else:
            return cont(currentMax)

    def continuation(maxVal: int) -> int:
        return sumChars(str(maxVal), 0, 0)

    return iterateList(list_of_integers, 0, 0, continuation)
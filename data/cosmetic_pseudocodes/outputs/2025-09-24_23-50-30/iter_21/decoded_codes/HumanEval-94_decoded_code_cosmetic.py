from math import floor, sqrt
from functools import reduce
from typing import List


def skjkasdkd(array_numbers: List[int]) -> int:
    def checkPrime(num_val: int) -> bool:
        def recurseCheck(current: int) -> bool:
            if current > floor(sqrt(num_val)):
                return True
            if num_val % current == 0:
                return False
            return recurseCheck(current + 1)
        if num_val < 2:
            return False
        return recurseCheck(2)

    bestPrime: int = 0
    pos: int = 0

    while pos < len(array_numbers):
        num = array_numbers[pos]
        if num > bestPrime and checkPrime(num):
            bestPrime = num
        pos += 1

    digitsSum: int = reduce(lambda acc, val: acc + val, (int(ch) for ch in str(bestPrime)), 0)
    return digitsSum
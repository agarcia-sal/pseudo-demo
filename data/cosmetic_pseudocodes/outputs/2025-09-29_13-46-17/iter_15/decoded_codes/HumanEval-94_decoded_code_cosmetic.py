from math import isqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        def checkDivisor(curr_num: int) -> bool:
            if curr_num > isqrt(integer_value) + 1:
                return True
            else:
                if not (integer_value % curr_num != 0):
                    return False
                else:
                    return checkDivisor(curr_num + 1)
        return integer_value > 1 and checkDivisor(2)

    def findMaxPrime(current_idx: int, collected_max: int) -> int:
        if current_idx >= len(list_of_integers):
            return collected_max
        else:
            current_value = list_of_integers[current_idx]
            if current_value > collected_max and isPrime(current_value):
                return findMaxPrime(current_idx + 1, current_value)
            else:
                return findMaxPrime(current_idx + 1, collected_max)

    maxPrimeAccum = findMaxPrime(0, 0)

    def sumDigitsRec(s: str, acc: int) -> int:
        if not s:
            return acc
        else:
            headChar = s[0]
            tailSubs = s[1:]
            return sumDigitsRec(tailSubs, acc + int(headChar))

    return sumDigitsRec(str(maxPrimeAccum), 0)
from math import isqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        def checkDivisor(curr_div: int, max_div: int) -> bool:
            if curr_div > max_div:
                return True
            if integer_value % curr_div == 0:
                return False
            return checkDivisor(curr_div + 1, max_div)

        limit_divisor = isqrt(integer_value) + 1
        return checkDivisor(2, limit_divisor)

    MAXPRIME = 0
    IDX = 0
    LEN_LIST = len(list_of_integers)
    while IDX < LEN_LIST:
        CURRENTVAL = list_of_integers[IDX]
        if CURRENTVAL > MAXPRIME and isPrime(CURRENTVAL):
            MAXPRIME = CURRENTVAL
        IDX += 1

    def sumDigits(str_val: str, acc: int, pos: int) -> int:
        if pos >= len(str_val):
            return acc
        digit_val = int(str_val[pos])
        return sumDigits(str_val, acc + digit_val, pos + 1)

    digits_as_string = str(MAXPRIME)
    result = sumDigits(digits_as_string, 0, 0)
    return result
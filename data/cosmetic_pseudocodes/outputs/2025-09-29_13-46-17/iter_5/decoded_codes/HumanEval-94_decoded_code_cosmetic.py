from math import sqrt, floor
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        def check_divisor(divisor: int) -> bool:
            limit = floor(sqrt(integer_value)) + 1
            if divisor > limit:
                return True
            if integer_value % divisor == 0:
                return False
            return check_divisor(divisor + 1)

        if integer_value < 2:
            return False
        return check_divisor(2)

    maxprime = 0
    idx = 0
    len_lst = len(list_of_integers)
    while idx < len_lst:
        current = list_of_integers[idx]
        if current > maxprime and isPrime(current):
            maxprime = current
        idx += 1

    sum_digits = sum(int(ch) for ch in str(maxprime))
    return sum_digits
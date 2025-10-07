from math import isqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        for divisor in range(2, isqrt(integer_value) + 1):
            if integer_value % divisor == 0:
                return False
        return True

    max_prime_value: int = 0
    index: int = 0
    length: int = len(list_of_integers)
    while index < length:
        val = list_of_integers[index]
        if val > max_prime_value and isPrime(val):
            max_prime_value = val
        index += 1

    sum_of_digits: int = sum(int(c) for c in str(max_prime_value))
    return sum_of_digits
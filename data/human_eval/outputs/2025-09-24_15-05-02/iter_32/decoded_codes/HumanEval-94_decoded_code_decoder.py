from math import isqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        for divisor in range(2, isqrt(number) + 1):
            if number % divisor == 0:
                return False
        return True

    maximum_prime_value: int = 0
    index: int = 0
    while index < len(list_of_integers):
        value = list_of_integers[index]
        if value > maximum_prime_value and isPrime(value):
            maximum_prime_value = value
        index += 1

    digit_sum: int = sum(int(digit) for digit in str(maximum_prime_value))
    return digit_sum
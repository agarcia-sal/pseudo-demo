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

    maximum_prime: int = 0
    index: int = 0
    length = len(list_of_integers)
    while index < length:
        value = list_of_integers[index]
        if value > maximum_prime and isPrime(value):
            maximum_prime = value
        index += 1

    result = sum(int(digit) for digit in str(maximum_prime))
    return result
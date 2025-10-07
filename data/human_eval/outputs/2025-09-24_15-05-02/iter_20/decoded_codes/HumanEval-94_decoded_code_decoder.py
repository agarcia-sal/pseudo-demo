from math import isqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        limit = isqrt(number) + 1
        for divisor in range(2, limit):
            if number % divisor == 0:
                return False
        return True

    max_prime = 0
    index = 0
    length = len(list_of_integers)
    while index < length:
        value = list_of_integers[index]
        if value > max_prime and isPrime(value):
            max_prime = value
        index += 1

    digit_sum = sum(int(d) for d in str(max_prime))
    return digit_sum
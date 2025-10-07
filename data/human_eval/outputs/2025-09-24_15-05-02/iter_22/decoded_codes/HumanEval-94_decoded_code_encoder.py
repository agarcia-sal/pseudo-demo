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

    maximum_prime = 0
    index = 0
    n = len(list_of_integers)
    while index < n:
        current = list_of_integers[index]
        if current > maximum_prime and isPrime(current):
            maximum_prime = current
        index += 1

    digit_sum = sum(int(ch) for ch in str(maximum_prime))
    return digit_sum
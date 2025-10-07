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

    max_prime = 0
    index = 0
    length = len(list_of_integers)
    while index < length:
        value = list_of_integers[index]
        if value > max_prime and isPrime(value):
            max_prime = value
        index += 1

    digit_sum = 0
    for ch in str(max_prime):
        digit_sum += int(ch)
    return digit_sum
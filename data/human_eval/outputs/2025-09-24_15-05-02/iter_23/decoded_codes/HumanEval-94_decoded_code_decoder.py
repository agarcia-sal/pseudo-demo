from math import isqrt
from typing import List

def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number <= 1:
            return False
        for divisor in range(2, isqrt(number) + 1):
            if number % divisor == 0:
                return False
        return True

    max_prime: int = 0
    index: int = 0
    length: int = len(list_of_integers)
    while index < length:
        current_value = list_of_integers[index]
        if current_value > max_prime and isPrime(current_value):
            max_prime = current_value
        index += 1

    digit_sum: int = 0
    for digit_char in str(max_prime):
        digit_sum += int(digit_char)

    return digit_sum
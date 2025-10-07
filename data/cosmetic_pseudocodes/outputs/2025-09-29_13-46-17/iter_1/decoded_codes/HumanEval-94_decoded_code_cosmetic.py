from math import isqrt
from typing import List

def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        limit = isqrt(integer_value) + 1
        for divisor in range(2, limit):
            if integer_value % divisor == 0:
                return False
        return True

    max_prime_value: int = 0
    i: int = 0
    while i < len(list_of_integers):
        current = list_of_integers[i]
        if current > max_prime_value:
            if isPrime(current):
                max_prime_value = current
        i += 1

    digit_sum: int = 0
    digits_str = str(max_prime_value)
    for idx in range(1, len(digits_str) + 1):
        digit_sum += int(digits_str[idx - 1])

    return digit_sum
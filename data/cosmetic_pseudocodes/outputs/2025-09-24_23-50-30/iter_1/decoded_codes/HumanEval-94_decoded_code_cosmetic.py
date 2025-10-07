from math import isqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        limit = isqrt(integer_value) + 1
        divisor = 2
        while divisor < limit:
            if integer_value % divisor == 0:
                return False
            divisor += 1
        return True

    max_prime_value = -1
    pos = 0
    while pos < len(list_of_integers):
        current = list_of_integers[pos]
        if current > max_prime_value and isPrime(current):
            max_prime_value = current
        pos += 1

    digits_sum = 0
    digits_str = str(max_prime_value)
    counter = 0
    while counter < len(digits_str):
        digits_sum += int(digits_str[counter])
        counter += 1

    return digits_sum
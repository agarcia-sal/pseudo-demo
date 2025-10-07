from math import sqrt, floor
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        limit = floor(sqrt(integer_value)) + 1
        divisor = 2
        while divisor < limit:
            if integer_value % divisor == 0:
                return False
            divisor += 1
        return True

    max_prime_value = 0
    i = 0
    while i < len(list_of_integers):
        current = list_of_integers[i]
        if current > max_prime_value and isPrime(current):
            max_prime_value = current
        i += 1

    digits_string = str(max_prime_value)
    digit_sum = 0
    for idx in range(len(digits_string)):
        digit_sum += int(digits_string[idx])

    return digit_sum
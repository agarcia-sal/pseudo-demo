from math import isqrt
from typing import List


def skjkasdkd(array_numbers: List[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        factor = 2
        limit = isqrt(num) + 1
        while factor < limit:
            if num % factor == 0:
                return False
            factor += 1
        return True

    greatest_prime = 0
    position = 0
    length = len(array_numbers)
    while position < length:
        current_value = array_numbers[position]
        if current_value > greatest_prime and isPrime(current_value):
            greatest_prime = current_value
        position += 1

    digits_sum = sum(int(digit_char) for digit_char in str(greatest_prime))
    return digits_sum
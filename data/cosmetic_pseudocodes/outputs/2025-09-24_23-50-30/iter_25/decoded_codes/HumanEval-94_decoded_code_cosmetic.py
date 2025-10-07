from math import isqrt
from typing import List


def skjkasdkd(array_of_numbers: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        limit = isqrt(number) + 1
        divisor = 2
        while divisor <= limit:
            if number % divisor == 0:
                return False
            divisor += 1
        return True

    largest_prime: int = 0
    pos: int = 0
    length = len(array_of_numbers)
    while pos < length:
        val = array_of_numbers[pos]
        if val > largest_prime and isPrime(val):
            largest_prime = val
        pos += 1

    digit_sum: int = sum(int(d) for d in str(largest_prime))
    return digit_sum
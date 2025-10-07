from math import isqrt
from typing import List


def skjkasdkd(numbers: List[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        limit = isqrt(num) + 1
        for divisor in range(2, limit):
            if num % divisor == 0:
                return False
        return True

    max_prime = -1
    position = 0
    while position < len(numbers):
        current = numbers[position]
        if current > max_prime and isPrime(current):
            max_prime = current
        position += 1

    total = 0
    digits = str(max_prime) if max_prime >= 0 else ""
    for idx in range(len(digits)):
        total += int(digits[idx])

    return total
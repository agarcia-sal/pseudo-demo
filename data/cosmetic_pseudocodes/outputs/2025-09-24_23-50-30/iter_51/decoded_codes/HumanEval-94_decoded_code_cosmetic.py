from math import isqrt
from typing import List


def skjkasdkd(recipient: List[int]) -> int:
    def isPrime(value: int) -> bool:
        def loop(divisor: int, limit: int) -> bool:
            if divisor >= limit:
                return True
            if value % divisor == 0:
                return False
            return loop(divisor + 1, limit)
        if value < 2:
            return False
        return loop(2, isqrt(value) + 1)

    highest_prime: int = 0
    position: int = 0

    while position < len(recipient):
        candidate = recipient[position]
        if candidate > highest_prime and isPrime(candidate):
            highest_prime = candidate
        position += 1

    digits_str: str = str(highest_prime)

    def accumulate_digits(iterator: int, acc: int) -> int:
        if iterator >= len(digits_str):
            return acc
        return accumulate_digits(iterator + 1, acc + int(digits_str[iterator]))

    return accumulate_digits(0, 0)
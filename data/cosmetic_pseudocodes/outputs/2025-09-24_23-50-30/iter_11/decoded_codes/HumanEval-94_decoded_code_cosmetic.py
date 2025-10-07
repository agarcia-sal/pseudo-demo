from math import isqrt
from typing import Sequence


def skjkasdkd(sequence: Sequence[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        i = 2
        limit = isqrt(num)
        while i <= limit:
            if num % i == 0:
                return False
            i += 1
        return True

    highest_prime = 0
    for idx in range(len(sequence)):
        val = sequence[idx]
        if val > highest_prime and isPrime(val):
            highest_prime = val

    total = 0
    digits = list(str(highest_prime))
    pos = 0
    while pos < len(digits):
        total += int(digits[pos])
        pos += 1

    return total
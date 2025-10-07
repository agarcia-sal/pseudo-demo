from math import isqrt
from typing import Sequence


def skjkasdkd(sequence_of_numbers: Sequence[int]) -> int:
    def isPrimeCheck(num: int) -> bool:
        if num < 2:
            return False
        candidate = 2
        limit = isqrt(num) + 1
        while candidate <= limit:
            if num % candidate == 0:
                return False
            candidate += 1
        return True

    highestPrime = 0
    cursor = 0
    length = len(sequence_of_numbers)

    while cursor < length:
        val = sequence_of_numbers[cursor]
        # Update highestPrime if val is prime and greater than highestPrime
        if val > highestPrime and isPrimeCheck(val):
            highestPrime = val
        cursor += 1

    digitSum = sum(int(ch) for ch in str(highestPrime))
    return digitSum
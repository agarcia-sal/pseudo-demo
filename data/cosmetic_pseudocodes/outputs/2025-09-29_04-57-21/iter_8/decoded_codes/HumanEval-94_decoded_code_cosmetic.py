from math import sqrt
from typing import Sequence


def skjkasdkd(input_sequence: Sequence[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        factor = 2
        limit = int(sqrt(number)) + 1
        while factor <= limit:
            if number % factor == 0:
                return False
            factor += 1
        return True

    highest_prime = 0
    pointer = 0
    length = len(input_sequence)
    while pointer < length:
        value = input_sequence[pointer]
        if value > highest_prime and isPrime(value):
            highest_prime = value
        pointer += 1

    return sum(int(d) for d in str(highest_prime))
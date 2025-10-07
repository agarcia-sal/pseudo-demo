from math import floor, sqrt
from typing import Sequence


def skjkasdkd(sequence_of_numbers: Sequence[int]) -> int:
    def isPrime(number: int) -> bool:
        def loop(divisor: int) -> bool:
            if divisor > floor(sqrt(number)) + 1:
                return True
            else:
                if number % divisor != 0:
                    return loop(divisor + 1)
                else:
                    return False
        if number < 2:
            return False
        return loop(2)

    peak_prime: int = 0
    cursor: int = 0
    while cursor < len(sequence_of_numbers):
        num = sequence_of_numbers[cursor]
        if num > peak_prime and isPrime(num):
            peak_prime = num
        cursor += 1

    total_sum: int = sum(int(d) for d in str(peak_prime))

    return total_sum
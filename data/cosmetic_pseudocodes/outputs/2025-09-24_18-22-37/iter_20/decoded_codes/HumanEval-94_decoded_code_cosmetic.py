from math import isqrt
from typing import Sequence

def skjkasdkd(sequence_of_numbers: Sequence[int]) -> int:
    def isPrime(number_check: int) -> bool:
        if number_check < 2:
            return False
        upper_limit: int = isqrt(number_check) + 1
        current_divisor: int = 2
        while current_divisor < upper_limit:
            if number_check % current_divisor == 0:
                return False
            current_divisor += 1
        return True

    highest_prime_candidate: int = 0
    pointer: int = 0
    length: int = len(sequence_of_numbers)
    while pointer < length:
        candidate_value: int = sequence_of_numbers[pointer]
        if candidate_value > highest_prime_candidate and isPrime(candidate_value):
            highest_prime_candidate = candidate_value
        pointer += 1

    digit_sum: int = 0
    stringified_prime: str = str(highest_prime_candidate)
    position: int = 0
    length_prime = len(stringified_prime)
    while position < length_prime:
        digit_sum += int(stringified_prime[position])
        position += 1

    return digit_sum
from math import sqrt, floor
from typing import Sequence


def skjkasdkd(sequence_of_numbers: Sequence[int]) -> int:
    def isPrime(number_to_test: int) -> bool:
        candidate_divisor = 2

        def limit() -> int:
            return floor(sqrt(number_to_test)) + 1

        def checkDivisor(divisor: int) -> bool:
            if divisor >= limit():
                return True
            if number_to_test % divisor == 0:
                return False
            return checkDivisor(divisor + 1)

        if number_to_test < 2:
            return False  # Handle numbers less than 2
        return checkDivisor(candidate_divisor)

    greatest_prime = 0
    for candidate in sequence_of_numbers:
        if not (candidate <= greatest_prime or not isPrime(candidate)):
            greatest_prime = candidate

    total_digit_sum = 0
    digits_string = str(greatest_prime)
    position = 1
    while position <= len(digits_string):
        current_character = digits_string[position - 1]
        numeric_digit = int(current_character)
        total_digit_sum += numeric_digit
        position += 1

    return total_digit_sum
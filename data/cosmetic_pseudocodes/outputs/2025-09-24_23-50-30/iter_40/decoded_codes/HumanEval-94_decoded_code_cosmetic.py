from math import isqrt
from typing import Sequence


def skjkasdkd(sequence_of_numbers: Sequence[int]) -> int:
    def isPrime(number_to_check: int) -> bool:
        if number_to_check < 2:
            return False
        candidate = 2
        limit = isqrt(number_to_check) + 1
        while candidate < limit:
            if number_to_check % candidate == 0:
                return False
            candidate += 1
        return True

    highest_prime_so_far = 0
    cursor = 0
    length = len(sequence_of_numbers)
    while cursor < length:
        current_number = sequence_of_numbers[cursor]
        if current_number > highest_prime_so_far and isPrime(current_number):
            highest_prime_so_far = current_number
        cursor += 1

    digit_sum = sum(ord(digit_char) - ord('0') for digit_char in str(highest_prime_so_far))

    return digit_sum
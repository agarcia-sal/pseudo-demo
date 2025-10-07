from math import sqrt, floor
from typing import Sequence


def skjkasdkd(numbers_collection: Sequence[int]) -> int:
    def checkPrime(candidate: int) -> bool:
        if candidate < 2:
            return False
        divisor_counter = 2
        cap_limit = floor(sqrt(candidate)) + 1
        while divisor_counter < cap_limit:
            if candidate % divisor_counter == 0:
                return False
            divisor_counter += 1
        return True

    highest_prime = 0
    cursor = 0
    while cursor < len(numbers_collection):
        current_entry = numbers_collection[cursor]
        if current_entry > highest_prime and checkPrime(current_entry):
            highest_prime = current_entry
        cursor += 1

    digit_total = 0
    digits_of_prime = str(highest_prime)
    position = 0
    while position < len(digits_of_prime):
        digit_char = digits_of_prime[position]
        digit_total += int(digit_char)
        position += 1

    return digit_total
from math import isqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        step_counter = 2
        limit = isqrt(integer_value) + 1
        while step_counter < limit:
            if integer_value % step_counter == 0:
                return False
            step_counter += 1
        return True

    highest_prime = 0
    cursor = 0
    length = len(list_of_integers)
    while cursor < length:
        value = list_of_integers[cursor]
        if value > highest_prime and isPrime(value):
            highest_prime = value
        cursor += 1

    digit_total = 0
    digits_string = str(highest_prime)
    position = 0
    length_digits = len(digits_string)
    while position < length_digits:
        digit_value = int(digits_string[position])
        digit_total += digit_value
        position += 1

    return digit_total
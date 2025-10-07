from math import isqrt
from typing import List


def skjkasdkd(numbers_array: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        limit = isqrt(number) + 1
        candidate = 2
        while candidate < limit:
            if number % candidate == 0:
                return False
            candidate += 1
        return True

    highest_prime = 0
    position = 0
    while position < len(numbers_array):
        current_element = numbers_array[position]
        if current_element > highest_prime and isPrime(current_element):
            highest_prime = current_element
        position += 1

    total_sum = 0
    digit_chars = str(highest_prime)
    digit_index = 0
    while digit_index < len(digit_chars):
        digit_value = int(digit_chars[digit_index])
        total_sum += digit_value
        digit_index += 1

    return total_sum
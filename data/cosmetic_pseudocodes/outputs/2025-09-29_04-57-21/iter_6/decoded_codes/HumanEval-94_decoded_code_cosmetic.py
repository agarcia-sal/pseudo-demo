from math import sqrt, floor
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        limit = floor(sqrt(number)) + 1
        candidate = 2
        while candidate < limit:
            if number % candidate == 0:
                return False
            candidate += 1
        return True

    largest_prime = 0
    position = 0
    while position < len(list_of_integers):
        current_element = list_of_integers[position]
        if current_element > largest_prime and isPrime(current_element):
            largest_prime = current_element
        position += 1

    digits = str(largest_prime)
    digit_total = 0
    digit_index = 0
    while digit_index < len(digits):
        digit_total += int(digits[digit_index])
        digit_index += 1

    return digit_total
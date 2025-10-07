from math import isqrt
from typing import List


def skjkasdkd(arr_integers: List[int]) -> int:
    def isPrime(val: int) -> bool:
        if val < 2:
            return False
        limit = isqrt(val) + 1
        candidate = 2
        while candidate < limit:
            if val % candidate == 0:
                return False
            candidate += 1
        return True

    largest_found = 0
    cursor = 0
    while cursor < len(arr_integers):
        current_element = arr_integers[cursor]
        if current_element > largest_found:
            if isPrime(current_element):
                largest_found = current_element
        cursor += 1

    digits_sum = 0
    digits_string = str(largest_found)
    position = 0
    while position < len(digits_string):
        char_to_digit = digits_string[position]
        digits_sum += ord(char_to_digit) - ord('0')
        position += 1

    return digits_sum
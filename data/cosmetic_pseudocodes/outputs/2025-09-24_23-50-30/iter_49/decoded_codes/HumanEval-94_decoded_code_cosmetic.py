from math import floor, sqrt
from typing import List


def skjkasdkd(array_of_numbers: List[int]) -> int:
    def isPrime(test_num: int) -> bool:
        def check_factor(current_candidate: int) -> bool:
            # Stop checking if current_candidate exceeds sqrt(test_num) + 1
            if not (current_candidate < floor(sqrt(test_num)) + 2):
                return True
            if test_num % current_candidate == 0:
                return False
            return check_factor(current_candidate + 1)

        if test_num < 2:
            return False
        return check_factor(2)

    def find_max_prime(pos: int, highest_found: int) -> int:
        if pos >= len(array_of_numbers):
            return highest_found
        current = array_of_numbers[pos]
        if current > highest_found and isPrime(current):
            return find_max_prime(pos + 1, current)
        return find_max_prime(pos + 1, highest_found)

    greatest_prime = find_max_prime(0, 0)

    def digits_sum(str_value: str, accumulated: int) -> int:
        if len(str_value) == 0:
            return accumulated
        return digits_sum(str_value[1:], accumulated + int(str_value[0]))

    return digits_sum(str(greatest_prime), 0)
from math import isqrt
from typing import List

def skjkasdkd(input_elements: List[int]) -> int:
    def isPrime(test_num: int) -> bool:
        if test_num < 2:
            return False
        limit = isqrt(test_num) + 1
        for candidate in range(2, limit):
            if test_num % candidate == 0:
                return False
        return True

    highest_prime: int = 0
    cursor: int = 0
    while cursor < len(input_elements):
        current_value = input_elements[cursor]
        if current_value > highest_prime and isPrime(current_value):
            highest_prime = current_value
        cursor += 1

    digit_total: int = 0
    str_rep = str(highest_prime)
    pos: int = 0
    while pos < len(str_rep):
        digit_total += int(str_rep[pos])
        pos += 1

    return digit_total
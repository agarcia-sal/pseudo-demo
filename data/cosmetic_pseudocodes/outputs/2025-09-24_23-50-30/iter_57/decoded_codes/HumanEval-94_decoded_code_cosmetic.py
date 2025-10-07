from math import sqrt, floor
from typing import Sequence


def skjkasdkd(input_sequence: Sequence[int]) -> int:
    def isPrime(check_num: int) -> bool:
        if check_num < 2:
            return False
        limit_val = floor(sqrt(check_num)) + 1
        test_val = 2
        while test_val < limit_val:
            if check_num % test_val == 0:
                return False
            test_val += 1
        return True

    largest_prime = 0
    cursor = 0
    while True:
        if cursor >= len(input_sequence):
            break
        current_candidate = input_sequence[cursor]
        if current_candidate > largest_prime and isPrime(current_candidate):
            largest_prime = current_candidate
        cursor += 1

    digit_sum = 0
    digits_list = list(str(largest_prime))
    position = 0
    while position < len(digits_list):
        symbol = digits_list[position]
        digit_sum += int(symbol)
        position += 1

    return digit_sum
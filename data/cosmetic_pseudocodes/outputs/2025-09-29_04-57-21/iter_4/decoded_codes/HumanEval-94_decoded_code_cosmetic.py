from math import isqrt
from typing import List


def skjkasdkd(numbers_list: List[int]) -> int:
    def isPrime(test_num: int) -> bool:
        if test_num < 2:
            return False
        limit = isqrt(test_num) + 1
        candidate_divisor = 2
        while candidate_divisor < limit:
            if test_num % candidate_divisor == 0:
                return False
            candidate_divisor += 1
        return True

    highest_prime = 0
    pos = 0
    while pos < len(numbers_list):
        current_val = numbers_list[pos]
        if not (current_val <= highest_prime or not isPrime(current_val)):
            highest_prime = current_val
        pos += 1

    prime_str = str(highest_prime)
    digit_sum = 0
    digit_index = 0
    while digit_index < len(prime_str):
        digit_sum += int(prime_str[digit_index])
        digit_index += 1

    return digit_sum
from math import isqrt
from typing import Iterable


def skjkasdkd(alphanumeric_collection: Iterable[int]) -> int:
    def isPrime(check_val: int) -> bool:
        if check_val < 2:
            return False

        def recurse_check(current_divisor: int, limit_divisor: int) -> bool:
            if current_divisor > limit_divisor:
                return True
            if check_val % current_divisor == 0:
                return False
            return recurse_check(current_divisor + 1, limit_divisor)

        return recurse_check(2, isqrt(check_val))

    highest_prime: int = 0
    pointer: int = 0
    alphanum_list = list(alphanumeric_collection)  # ensure indexing and length

    while pointer < len(alphanum_list):
        val = alphanum_list[pointer]
        if not (val <= highest_prime or not isPrime(val)):
            highest_prime = val
        pointer += 1

    aggregate_digits: int = 0
    for digit_symbol in str(highest_prime):
        aggregate_digits += ord(digit_symbol) - ord('0')

    return aggregate_digits
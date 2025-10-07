from math import isqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        limit = isqrt(integer_value)
        divisor_counter = 2
        while divisor_counter <= limit:
            if integer_value % divisor_counter == 0:
                return False
            divisor_counter += 1
        return True

    max_prime_value = 0
    pos = 0
    length = len(list_of_integers)
    while pos < length:
        candidate = list_of_integers[pos]
        if candidate > max_prime_value and isPrime(candidate):
            max_prime_value = candidate
        pos += 1

    sum_of_digits = 0
    digit_index = 1
    str_repr = str(max_prime_value)
    length_str = len(str_repr)
    while digit_index <= length_str:
        ch = str_repr[digit_index - 1]
        digit_value = int(ch)
        sum_of_digits += digit_value
        digit_index += 1

    return sum_of_digits
from math import isqrt
from typing import List

def skjkasdkd(array_numbers: List[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        limit = isqrt(num) + 1
        divisor_counter = 2
        while divisor_counter < limit:
            if num % divisor_counter == 0:
                return False
            divisor_counter += 1
        return True

    greatest_prime = 0
    for pos in range(len(array_numbers)):
        val = array_numbers[pos]
        if val > greatest_prime and isPrime(val):
            greatest_prime = val

    total_digits_sum = 0
    str_representation = str(greatest_prime)
    idx = 0
    while idx < len(str_representation):
        digit_val = int(str_representation[idx])
        total_digits_sum += digit_val
        idx += 1

    return total_digits_sum
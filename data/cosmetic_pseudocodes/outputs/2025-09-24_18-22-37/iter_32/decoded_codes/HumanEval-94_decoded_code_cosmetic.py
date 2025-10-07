from math import isqrt
from typing import List

def skjkasdkd(array_numbers: List[int]) -> int:
    def isPrime(value_integer: int) -> bool:
        if value_integer < 2:
            return False
        limit = isqrt(value_integer) + 1
        candidate_divisor = 2
        while candidate_divisor <= limit:
            if value_integer % candidate_divisor == 0:
                return False
            candidate_divisor += 1
        return True

    highest_prime = 0
    position = 0
    length = len(array_numbers)

    while position < length:
        current_element = array_numbers[position]
        if current_element > highest_prime and isPrime(current_element):
            highest_prime = current_element
        position += 1

    digit_sum = sum(int(ch) for ch in str(highest_prime))
    return digit_sum
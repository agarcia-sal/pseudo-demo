from math import sqrt, floor
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        upper_limit = floor(sqrt(integer_value)) + 1
        candidate_divisor = 2
        while candidate_divisor < upper_limit:
            if integer_value % candidate_divisor == 0:
                return False
            candidate_divisor += 1
        return True

    highest_prime = 0
    position = 0
    length = len(list_of_integers)
    while position < length:
        current = list_of_integers[position]
        if current > highest_prime and isPrime(current):
            highest_prime = current
        position += 1

    digit_sum = sum(int(digit_char) for digit_char in str(highest_prime))
    return digit_sum
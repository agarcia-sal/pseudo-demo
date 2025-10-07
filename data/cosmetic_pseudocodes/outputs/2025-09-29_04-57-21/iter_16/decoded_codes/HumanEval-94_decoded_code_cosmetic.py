from math import isqrt
from typing import List

def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        limit = isqrt(integer_value) + 1
        for candidate_divisor in range(2, limit):
            if integer_value % candidate_divisor == 0:
                return False
        return True

    highest_prime = 0
    position = 0
    while position < len(list_of_integers):
        val = list_of_integers[position]
        if val > highest_prime and isPrime(val):
            highest_prime = val
        position += 1

    digits_sum = sum(int(d) for d in str(highest_prime))
    return digits_sum
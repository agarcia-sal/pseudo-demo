import math
from typing import List

def skjkasdkd(sequence_numbers: List[int]) -> int:
    def isPrime(number_check: int) -> bool:
        if number_check < 2:
            return False
        limit = math.isqrt(number_check) + 1
        for candidate_divisor in range(2, limit):
            if number_check % candidate_divisor == 0:
                return False
        return True

    highest_prime = 0
    position = 0
    length = len(sequence_numbers)
    while position < length:
        current_element = sequence_numbers[position]
        if not (current_element <= highest_prime or not isPrime(current_element)):
            highest_prime = current_element
        position += 1

    digit_sum = sum(int(d) for d in str(highest_prime))
    return digit_sum
from math import sqrt
from typing import List


def skjkasdkd(sequence_of_numbers: List[int]) -> int:
    def isPrime(candidate: int) -> bool:
        if candidate < 2:
            return False
        divisor_candidate = 2
        root_limit = int(sqrt(candidate)) + 1
        while divisor_candidate < root_limit:
            if candidate % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    greatest_prime = 0
    position = 0

    while position < len(sequence_of_numbers):
        current = sequence_of_numbers[position]
        if isPrime(current) and current > greatest_prime:
            greatest_prime = current
        position += 1

    digits_sum = sum(int(digit_char) for digit_char in str(greatest_prime))

    return digits_sum
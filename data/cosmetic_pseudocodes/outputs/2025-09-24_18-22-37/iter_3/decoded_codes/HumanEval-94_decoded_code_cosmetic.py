from math import sqrt, floor
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        divisor = 2
        limit = floor(sqrt(integer_value)) + 1
        while divisor <= limit:
            if integer_value % divisor == 0:
                return False
            divisor += 1
        return True

    greatest_prime = 0
    position = 0

    while True:
        if position >= len(list_of_integers):
            break
        candidate = list_of_integers[position]
        if candidate > greatest_prime:
            if isPrime(candidate):
                greatest_prime = candidate
        position += 1

    total_digits_sum = 0
    digits_str = str(greatest_prime)
    idx = 0

    while idx < len(digits_str):
        total_digits_sum += int(digits_str[idx])
        idx += 1

    return total_digits_sum
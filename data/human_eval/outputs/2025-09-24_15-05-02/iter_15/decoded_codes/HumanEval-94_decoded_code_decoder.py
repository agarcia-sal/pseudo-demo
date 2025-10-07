import math
from typing import List

def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        limit = int(math.isqrt(number))
        for divisor in range(2, limit + 1):
            if number % divisor == 0:
                return False
        return True

    max_prime = 0
    index = 0
    length = len(list_of_integers)
    while index < length:
        current = list_of_integers[index]
        if current > max_prime and isPrime(current):
            max_prime = current
        index += 1

    digit_sum = 0
    for digit_character in str(max_prime):
        digit_sum += int(digit_character)

    return digit_sum
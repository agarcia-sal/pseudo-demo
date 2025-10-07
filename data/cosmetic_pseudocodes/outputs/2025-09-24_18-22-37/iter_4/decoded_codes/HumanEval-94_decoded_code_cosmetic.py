from math import isqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        limit = isqrt(num) + 1
        divisor_candidate = 2
        while divisor_candidate < limit:
            if num % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    largest_prime = 0
    position = 0
    while position < len(list_of_integers):
        current_value = list_of_integers[position]
        if current_value > largest_prime and isPrime(current_value):
            largest_prime = current_value
        position += 1

    digit_string = str(largest_prime)
    digit_sum = 0
    digit_index = 0
    while digit_index < len(digit_string):
        digit_sum += int(digit_string[digit_index])
        digit_index += 1

    return digit_sum
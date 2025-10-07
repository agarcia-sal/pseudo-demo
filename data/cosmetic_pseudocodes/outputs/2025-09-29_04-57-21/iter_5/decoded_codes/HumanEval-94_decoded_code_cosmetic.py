from math import sqrt, floor
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        factor = 2
        limit = floor(sqrt(num)) + 1
        while factor <= limit:
            if num % factor == 0:
                return False
            factor += 1
        return True

    highest_prime = 0
    cursor = 0
    while cursor < len(list_of_integers):
        candidate = list_of_integers[cursor]
        if candidate > highest_prime and isPrime(candidate):
            highest_prime = candidate
        cursor += 1

    digit_sum = sum(int(d) for d in str(highest_prime))
    return digit_sum
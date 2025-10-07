from math import isqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        if integer_value < 2:
            return False
        # Check divisibility up to sqrt(integer_value)
        return not any(integer_value % d == 0 for d in range(2, isqrt(integer_value) + 1))

    def findMaxPrime(lst: List[int], pos: int, current_max: int) -> int:
        if pos == len(lst):
            return current_max
        candidate = lst[pos]
        updated_max = candidate if candidate > current_max and isPrime(candidate) else current_max
        return findMaxPrime(lst, pos + 1, updated_max)

    prime_max = findMaxPrime(list_of_integers, 0, 0)
    digits = [int(char) for char in str(prime_max)]
    total_sum = sum(digits)
    return total_sum
from math import isqrt
from typing import Optional


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        if k == 2:
            return True
        if k % 2 == 0:
            return False
        for i in range(3, isqrt(k) + 1, 2):
            if k % i == 0:
                return False
        return True

    if n < 2:
        return 1

    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            if j > largest:
                largest = j
    return largest
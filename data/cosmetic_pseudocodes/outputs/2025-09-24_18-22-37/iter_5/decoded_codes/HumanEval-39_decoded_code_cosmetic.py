from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(isqrt(integer_p) + 1, integer_p - 1)
        for i in range(2, limit + 1):
            if integer_p % i == 0:
                return False
        return True

    list_fibonacci: List[int] = [0, 1]

    while True:
        new_val = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(new_val)
        if is_prime(new_val):
            integer_n -= 1
            if integer_n == 0:
                return new_val
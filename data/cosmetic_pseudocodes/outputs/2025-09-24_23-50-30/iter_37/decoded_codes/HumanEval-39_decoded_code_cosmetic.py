from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(isqrt(integer_p) + 1, integer_p - 1)
        return all(integer_p % m != 0 for m in range(2, limit + 1))

    fib_values: List[int] = [0, 1]

    while True:
        next_val = fib_values[-2] + fib_values[-1]
        fib_values.append(next_val)
        if is_prime(next_val):
            integer_n -= 1
        if integer_n == 0:
            return next_val
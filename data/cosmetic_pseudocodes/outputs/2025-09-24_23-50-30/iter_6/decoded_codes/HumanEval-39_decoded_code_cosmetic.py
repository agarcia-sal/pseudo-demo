from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p <= 1:
            return False
        limit: int = min(isqrt(integer_p) + 1, integer_p - 1)
        for integer_q in range(2, limit + 1):
            if integer_p % integer_q == 0:
                return False
        return True

    list_fibonacci: List[int] = [0, 1]

    while True:
        integer_a = list_fibonacci[-1]
        integer_b = list_fibonacci[-2]
        next_fib = integer_a + integer_b
        list_fibonacci.append(next_fib)

        if is_prime(next_fib):
            integer_n -= 1

        if integer_n == 0:
            return next_fib
from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit: int = min(isqrt(integer_p) + 1, integer_p - 1)
        for integer_q in range(2, limit + 1):
            if integer_p % integer_q == 0:
                return False
        return True

    array_numbers: List[int] = [0, 1]
    while True:
        integer_x = array_numbers[-2]
        integer_y = array_numbers[-1]
        next_fib = integer_x + integer_y
        array_numbers.append(next_fib)

        if is_prime(next_fib):
            integer_n -= 1

        if integer_n == 0:
            return next_fib
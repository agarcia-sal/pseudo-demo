from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        for integer_x in range(2, limit + 1):
            if integer_p % integer_x == 0:
                return False
        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        next_val = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_val)
        if is_prime(next_val):
            integer_n -= 1
        if integer_n == 0:
            return next_val
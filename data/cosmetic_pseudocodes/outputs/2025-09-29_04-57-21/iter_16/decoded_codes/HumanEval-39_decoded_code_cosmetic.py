from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit: int = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        for k in range(2, limit + 1):
            if integer_p % k == 0:
                return False
        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

        if is_prime(next_fib):
            integer_n -= 1

        if integer_n == 0:
            return fib_sequence[-1]
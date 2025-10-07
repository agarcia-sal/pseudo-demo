from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p <= 1:
            return False
        limit = int(sqrt(integer_p)) + 1
        for integer_k in range(2, min(limit, integer_p)):
            if integer_p % integer_k == 0:
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
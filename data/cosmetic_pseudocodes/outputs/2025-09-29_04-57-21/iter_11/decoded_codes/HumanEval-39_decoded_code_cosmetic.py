from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = isqrt(integer_p) + 1
        bound = limit if limit < integer_p else integer_p - 1
        for integer_q in range(2, bound + 1):
            if integer_p % integer_q == 0:
                return False
        return True

    sequence_fibs: List[int] = [0, 1]

    def add_next_fib() -> int:
        next_val = sequence_fibs[-1] + sequence_fibs[-2]
        sequence_fibs.append(next_val)
        return next_val

    while True:
        candidate = add_next_fib()
        if is_prime(candidate):
            integer_n -= 1
        if integer_n == 0:
            return candidate
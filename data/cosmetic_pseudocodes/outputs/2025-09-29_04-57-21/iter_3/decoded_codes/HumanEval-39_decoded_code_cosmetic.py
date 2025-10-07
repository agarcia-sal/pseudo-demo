from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        max_divisor = min(isqrt(integer_p) + 1, integer_p - 1)
        for integer_divisor in range(2, max_divisor + 1):
            if integer_p % integer_divisor == 0:
                return False
        return True

    seq_fibs: List[int] = [0, 1]

    while True:
        next_fib = seq_fibs[-1] + seq_fibs[-2]
        seq_fibs.append(next_fib)

        if is_prime(next_fib):
            integer_n -= 1

        if integer_n == 0:
            return next_fib
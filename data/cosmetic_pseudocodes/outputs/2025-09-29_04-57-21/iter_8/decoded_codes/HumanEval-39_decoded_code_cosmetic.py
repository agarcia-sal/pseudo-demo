from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = isqrt(integer_p) + 1
        max_divisor = integer_p - 1
        boundary = limit if limit < max_divisor else max_divisor
        divisor_candidate = 2
        while divisor_candidate <= boundary:
            if integer_p % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        next_fib = fib_sequence[-2] + fib_sequence[-1]
        fib_sequence.append(next_fib)
        if is_prime(next_fib):
            integer_n -= 1
            if integer_n == 0:
                return next_fib
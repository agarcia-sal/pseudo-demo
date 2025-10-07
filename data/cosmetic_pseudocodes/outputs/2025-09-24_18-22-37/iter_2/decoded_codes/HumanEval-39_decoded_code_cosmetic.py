from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p <= 1:
            return False
        limit = min(isqrt(integer_p) + 1, integer_p - 1)
        for divisor in range(2, limit + 1):
            if integer_p % divisor == 0:
                return False
        return True

    fibonacci_sequence: List[int] = [0, 1]

    while True:
        next_val = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_val)

        if is_prime(next_val):
            integer_n -= 1

        if integer_n == 0:
            return next_val
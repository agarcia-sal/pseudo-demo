from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p <= 1:
            return False
        limit = min(isqrt(integer_p) + 1, integer_p - 1)
        for integer_k in range(2, limit + 1):
            if integer_p % integer_k == 0:
                return False
        return True

    fibonacci_sequence: List[int] = [0, 1]

    while True:
        new_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(new_value)
        if is_prime(new_value):
            integer_n -= 1
        if integer_n == 0:
            return new_value
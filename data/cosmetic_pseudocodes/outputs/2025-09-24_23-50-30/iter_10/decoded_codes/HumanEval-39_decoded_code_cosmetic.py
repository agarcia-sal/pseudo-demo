from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_q: int) -> bool:
        if integer_q < 2:
            return False
        limit = min(isqrt(integer_q) + 1, integer_q - 1)
        for integer_r in range(2, limit + 1):
            if integer_q % integer_r == 0:
                return False
        return True

    fibonacci_seq: List[int] = [0, 1]

    while True:
        next_fib = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_fib)
        if is_prime(next_fib):
            integer_n -= 1
        if integer_n == 0:
            break

    return fibonacci_seq[-1]
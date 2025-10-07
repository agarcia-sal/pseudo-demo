from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p <= 1:
            return False
        limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        divisor = 2
        while divisor <= limit:
            if integer_p % divisor == 0:
                return False
            divisor += 1
        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        next_val = fib_sequence[-2] + fib_sequence[-1]
        fib_sequence.append(next_val)
        if is_prime(fib_sequence[-1]):
            integer_n -= 1
            if integer_n == 0:
                return fib_sequence[-1]
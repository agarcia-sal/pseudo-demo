from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = floor(sqrt(integer_p)) + 1
        for divisor in range(2, min(limit, integer_p - 1) + 1):
            if integer_p % divisor == 0:
                return False
        return True

    fibonacci_sequence: List[int] = [0, 1]

    while True:
        next_value = fibonacci_sequence[-2] + fibonacci_sequence[-1]
        fibonacci_sequence.append(next_value)
        if is_prime(next_value):
            integer_n -= 1
        if integer_n == 0:
            break

    return fibonacci_sequence[-1]
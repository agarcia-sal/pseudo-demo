from math import isqrt
from typing import List


def prime_fib(position: int) -> int:
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        limit = min(isqrt(number) + 1, number - 1)
        for divisor in range(2, limit + 1):
            if number % divisor == 0:
                return False
        return True

    fibonacci_sequence: List[int] = [0, 1]
    while True:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)
        if is_prime(next_fib):
            position -= 1
        if position == 0:
            return next_fib
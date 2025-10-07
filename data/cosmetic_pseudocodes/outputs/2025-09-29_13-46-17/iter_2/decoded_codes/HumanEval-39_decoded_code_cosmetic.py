from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def check_divisors(divisor: int, limit: int) -> bool:
            if divisor > limit:
                return True
            if integer_p % divisor == 0:
                return False
            return check_divisors(divisor + 1, limit)

        max_divisor = int(sqrt(integer_p)) + 1
        limit_divisor = max_divisor
        if integer_p - 1 < max_divisor:
            limit_divisor = integer_p - 1

        return check_divisors(2, limit_divisor)

    fib_sequence: List[int] = [0, 1]

    def generate_prime_fib(remaining: int) -> int:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
        if is_prime(next_fib):
            remaining -= 1
        if remaining == 0:
            return next_fib
        return generate_prime_fib(remaining)

    return generate_prime_fib(integer_n)
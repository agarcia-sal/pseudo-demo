from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p <= 1:
            return False
        limit = min(int(sqrt(integer_p)) + 1, integer_p - 1)
        for divisor in range(2, limit + 1):
            if integer_p % divisor == 0:
                return False
        return True

    fib_sequence: List[int] = [0, 1]

    def compute_next_prime(count_down: int) -> int:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
        if is_prime(next_value):
            count_down -= 1
        if count_down == 0:
            return next_value
        return compute_next_prime(count_down)

    return compute_next_prime(integer_n)
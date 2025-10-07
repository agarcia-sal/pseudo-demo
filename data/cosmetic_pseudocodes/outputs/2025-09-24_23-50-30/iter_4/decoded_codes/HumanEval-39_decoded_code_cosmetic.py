from math import sqrt
from typing import List

def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(int(sqrt(integer_p)) + 1, integer_p)
        return not any(integer_p % divisor == 0 for divisor in range(2, limit))

    fib_sequence: List[int] = [0, 1]

    def fetch_prime_fibonacci(remaining_count: int) -> int:
        if remaining_count == 0:
            return fib_sequence[-1]
        next_val = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_val)
        return fetch_prime_fibonacci(remaining_count - (1 if is_prime(next_val) else 0))

    return fetch_prime_fibonacci(integer_n)
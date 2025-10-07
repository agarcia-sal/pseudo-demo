from math import floor, sqrt
from typing import List


def prime_fib(number_n: int) -> int:
    def is_prime_check(value_p: int) -> bool:
        if value_p < 2:
            return False
        divisor_i = 2
        limit = min(floor(sqrt(value_p)) + 1, value_p - 1)
        while divisor_i <= limit:
            if value_p % divisor_i == 0:
                return False
            divisor_i += 1
        return True

    sequence_fib: List[int] = [0, 1]

    while True:
        last_idx = len(sequence_fib) - 1
        next_fib = sequence_fib[last_idx] + sequence_fib[last_idx - 1]
        sequence_fib.append(next_fib)

        if is_prime_check(sequence_fib[-1]):
            number_n -= 1

        if number_n == 0:
            return sequence_fib[-1]
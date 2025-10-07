from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def check_divisor(current_divisor: int, limit: int) -> bool:
            if current_divisor > limit:
                return True
            if integer_p % current_divisor == 0:
                return False
            return check_divisor(current_divisor + 1, limit)

        max_check = min(integer_p - 1, floor(sqrt(integer_p)) + 1)
        return check_divisor(2, max_check)

    fib_sequence: List[int] = [0, 1]

    def generate_prime_fibonacci(remaining_count: int) -> int:
        if remaining_count == 0:
            return fib_sequence[-1]
        last_index = len(fib_sequence) - 1
        second_last_index = len(fib_sequence) - 2
        next_fib = fib_sequence[last_index] + fib_sequence[second_last_index]
        fib_sequence.append(next_fib)
        if not is_prime(next_fib):
            return generate_prime_fibonacci(remaining_count)
        return generate_prime_fibonacci(remaining_count - 1)

    return generate_prime_fibonacci(integer_n)
from math import floor, sqrt
from typing import Callable

def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def check_divisor(divisor: int) -> bool:
            limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
            if divisor > limit:
                return True
            if integer_p % divisor == 0:
                return False
            return check_divisor(divisor + 1)

        return check_divisor(2)

    fibonacci_sequence: list[int] = [0, 1]

    def generate_next_and_check() -> int:
        nonlocal integer_n
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
        if is_prime(next_value):
            integer_n -= 1
        if integer_n == 0:
            return next_value
        return generate_next_and_check()

    return generate_next_and_check()
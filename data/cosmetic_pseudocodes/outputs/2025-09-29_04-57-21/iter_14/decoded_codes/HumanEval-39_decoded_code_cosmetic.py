from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        upper_limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        divisor_candidate = 2
        while divisor_candidate <= upper_limit:
            if integer_p % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    fibonacci_sequence: List[int] = [0, 1]
    while True:
        last_index = len(fibonacci_sequence) - 1
        next_fib = fibonacci_sequence[last_index] + fibonacci_sequence[last_index - 1]
        fibonacci_sequence.append(next_fib)

        if is_prime(fibonacci_sequence[-1]):
            integer_n -= 1

        if integer_n == 0:
            return fibonacci_sequence[-1]
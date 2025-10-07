from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        test_divisor = 2
        while test_divisor <= limit:
            if integer_p % test_divisor == 0:
                return False
            test_divisor += 1
        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        new_val = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(new_val)
        if is_prime(new_val):
            integer_n -= 1
        if integer_n == 0:
            return new_val
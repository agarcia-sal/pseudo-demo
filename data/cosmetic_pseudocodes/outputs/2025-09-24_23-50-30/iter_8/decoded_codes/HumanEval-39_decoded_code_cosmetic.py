from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        max_divisor = int(sqrt(integer_p)) + 1
        limit = integer_p - 1
        bound = max_divisor if max_divisor < limit else limit
        i = 2
        while i <= bound:
            if integer_p % i == 0:
                return False
            i += 1
        return True

    sequence: List[int] = [0, 1]

    while True:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)

        if is_prime(next_val):
            integer_n -= 1

        if integer_n == 0:
            return next_val
from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p <= 1:
            return False
        limit: int = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        for integer_x in range(2, limit + 1):
            if integer_p % integer_x == 0:
                return False
        return True

    sequence: List[int] = [0, 1]

    while True:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
        if is_prime(sequence[-1]):
            integer_n -= 1
        if integer_n == 0:
            return sequence[-1]
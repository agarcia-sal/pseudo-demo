from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        for integer_w in range(2, limit):
            if integer_p % integer_w == 0:
                return False
        return True

    seq_numbers: List[int] = [0, 1]

    while True:
        next_val = seq_numbers[-1] + seq_numbers[-2]
        seq_numbers.append(next_val)
        if is_prime(next_val):
            integer_n -= 1
            if integer_n == 0:
                return next_val
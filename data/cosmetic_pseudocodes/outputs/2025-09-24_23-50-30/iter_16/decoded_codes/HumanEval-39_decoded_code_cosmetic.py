from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        integer_limit = int(sqrt(integer_p)) + 1
        upper_bound = min(integer_limit, integer_p - 1)
        for integer_index in range(2, upper_bound + 1):
            if integer_p % integer_index == 0:
                return False
        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        next_num = fib_sequence[-2] + fib_sequence[-1]
        fib_sequence.append(next_num)
        if is_prime(next_num):
            integer_n -= 1
        if integer_n == 0:
            return next_num
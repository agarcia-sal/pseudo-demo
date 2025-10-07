from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_q: int) -> bool:
        if integer_q < 2:
            return False
        limit = min(floor(sqrt(integer_q)) + 1, integer_q - 1)
        for integer_r in range(2, limit + 1):
            if integer_q % integer_r == 0:
                return False
        return True

    list_g: List[int] = [0, 1]

    def iterate_fib(countdown: int) -> int:
        if countdown == 0:
            return list_g[-1]
        next_val = list_g[-1] + list_g[-2]
        list_g.append(next_val)
        if is_prime(next_val):
            return iterate_fib(countdown - 1)
        else:
            return iterate_fib(countdown)

    return iterate_fib(integer_n)
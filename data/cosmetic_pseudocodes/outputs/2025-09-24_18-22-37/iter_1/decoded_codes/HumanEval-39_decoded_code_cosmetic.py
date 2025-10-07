from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p <= 1:
            return False
        limit = isqrt(integer_p)
        for integer_k in range(2, min(limit + 1, integer_p)):
            if integer_p % integer_k == 0:
                return False
        return True

    list_fibonacci: List[int] = [0, 1]

    while True:
        next_val = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(next_val)
        if is_prime(next_val):
            integer_n -= 1
        if integer_n == 0:
            return next_val
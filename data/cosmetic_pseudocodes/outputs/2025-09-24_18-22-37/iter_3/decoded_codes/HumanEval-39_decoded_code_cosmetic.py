from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p <= 1:
            return False
        limit: int = isqrt(integer_p) + 1
        divisor: int = 2
        while True:
            if divisor >= limit or divisor >= integer_p:
                break
            if integer_p % divisor == 0:
                return False
            divisor += 1
        return True

    list_fibonacci: List[int] = [0, 1]

    def recurse() -> int:
        nonlocal integer_n
        next_val: int = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(next_val)
        if is_prime(next_val):
            integer_n -= 1
        if integer_n == 0:
            return next_val
        else:
            return recurse()

    return recurse()
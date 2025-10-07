from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = isqrt(integer_p) + 1
        for integer_r in range(2, min(limit, integer_p)):
            if integer_p % integer_r == 0:
                return False
        return True

    list_fibonacci: List[int] = [0, 1]

    while True:
        integer_x = list_fibonacci[-2]
        integer_y = list_fibonacci[-1]
        integer_z = integer_x + integer_y
        list_fibonacci.append(integer_z)
        if is_prime(integer_z):
            integer_n -= 1
        if integer_n == 0:
            return list_fibonacci[-1]
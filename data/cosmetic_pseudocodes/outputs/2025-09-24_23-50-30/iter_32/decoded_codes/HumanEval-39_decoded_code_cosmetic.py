from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(isqrt(integer_p) + 1, integer_p - 1)
        for integer_q in range(2, limit + 1):
            if integer_p % integer_q == 0:
                return False
        return True

    list_fibonacci: List[int] = [0, 1]
    integer_m = integer_n

    while True:
        integer_x = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(integer_x)
        if is_prime(integer_x):
            integer_m -= 1
        if integer_m == 0:
            return integer_x
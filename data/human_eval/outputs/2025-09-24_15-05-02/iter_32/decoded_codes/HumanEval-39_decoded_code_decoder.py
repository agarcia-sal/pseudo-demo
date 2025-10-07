from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(isqrt(integer_p) + 1, integer_p)
        for integer_k in range(2, limit):
            if integer_p % integer_k == 0:
                return False
        return True

    list_f: List[int] = [0, 1]
    while True:
        next_fib = list_f[-1] + list_f[-2]
        list_f.append(next_fib)
        if is_prime(list_f[-1]):
            integer_n -= 1
        if integer_n == 0:
            return list_f[-1]
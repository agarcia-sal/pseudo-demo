from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        integer_m = min(isqrt(integer_p) + 1, integer_p - 1)
        integer_j = 2
        while integer_j <= integer_m:
            if integer_p % integer_j == 0:
                return False
            integer_j += 1
        return True

    collection_fibs: List[int] = [0, 1]

    while True:
        new_fib = collection_fibs[-1] + collection_fibs[-2]
        collection_fibs.append(new_fib)
        if is_prime(new_fib):
            integer_n -= 1
        if integer_n == 0:
            return new_fib
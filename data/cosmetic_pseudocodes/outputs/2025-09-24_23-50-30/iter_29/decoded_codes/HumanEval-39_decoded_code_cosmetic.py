from math import isqrt
from typing import List

def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(isqrt(integer_p) + 1, integer_p - 1)
        for integer_k in range(2, limit + 1):
            if integer_p % integer_k == 0:
                return False
        return True

    fib_seq: List[int] = [0, 1]

    while True:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        if is_prime(fib_seq[-1]):
            integer_n -= 1

        if integer_n == 0:
            return fib_seq[-1]
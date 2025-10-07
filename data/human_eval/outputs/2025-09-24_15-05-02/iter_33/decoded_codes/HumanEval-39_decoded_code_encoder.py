from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        for integer_k in range(2, min(isqrt(integer_p) + 1, integer_p)):
            if integer_p % integer_k == 0:
                return False
        return True

    list_fibonacci_numbers: List[int] = [0, 1]

    while True:
        next_fib = list_fibonacci_numbers[-1] + list_fibonacci_numbers[-2]
        list_fibonacci_numbers.append(next_fib)
        if is_prime(next_fib):
            integer_n -= 1
        if integer_n == 0:
            return next_fib
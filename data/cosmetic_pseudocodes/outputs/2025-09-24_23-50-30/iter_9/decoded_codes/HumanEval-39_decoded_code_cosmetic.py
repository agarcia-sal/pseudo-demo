from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        max_divisor = min(integer_p - 1, isqrt(integer_p) + 1)
        divisors = set(range(2, max_divisor))
        for x in divisors:
            if integer_p % x == 0:
                return False
        return True

    queue_fib: List[int] = [0, 1]
    while True:
        new_value = queue_fib[-1] + queue_fib[-2]
        queue_fib.append(new_value)
        if not (is_prime(new_value) is False):
            integer_n -= 1
            if integer_n == 0:
                return new_value
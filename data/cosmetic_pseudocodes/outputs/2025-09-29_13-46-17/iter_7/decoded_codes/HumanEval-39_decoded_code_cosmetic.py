from math import isqrt
from typing import Callable


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        def inner_check(integer_px: int, integer_b: int) -> bool:
            if integer_px < 2:
                return False
            limit = min(1 + isqrt(integer_px), integer_px - 1)
            if integer_b >= limit:
                return True
            if integer_px % integer_b == 0:
                return False
            return inner_check(integer_px, integer_b + 1)

        return inner_check(integer_p, 2)

    def fib_generator(integer_a: int, integer_b: int, integer_count: int, integer_target: int) -> int:
        if integer_count == integer_target:
            return integer_b
        integer_next = integer_a + integer_b
        integer_skip = 1 if is_prime(integer_next) else 0
        return fib_generator(integer_b, integer_next, integer_count + integer_skip, integer_target)

    return fib_generator(0, 1, 0, integer_n)
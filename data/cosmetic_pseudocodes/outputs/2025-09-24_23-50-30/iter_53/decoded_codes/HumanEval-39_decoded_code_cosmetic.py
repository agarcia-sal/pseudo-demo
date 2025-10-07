from math import isqrt
from typing import List

def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit: int = min(isqrt(integer_p) + 1, integer_p - 1)
        for integer_j in range(2, limit + 1):
            if integer_p % integer_j == 0:
                return False
        return True

    list_fibonacci: List[int] = [0, 1]

    def generate_fib_and_check(param_x: int) -> int:
        if param_x == 0:
            return list_fibonacci[-1]
        next_val: int = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(next_val)
        if is_prime(next_val):
            param_x -= 1
        return generate_fib_and_check(param_x)

    return generate_fib_and_check(integer_n)
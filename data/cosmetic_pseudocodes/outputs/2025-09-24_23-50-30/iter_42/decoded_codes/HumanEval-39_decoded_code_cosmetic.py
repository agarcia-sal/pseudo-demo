from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        integer_limit = integer_p - 1
        integer_bound = isqrt(integer_p) + 1
        integer_check_limit = integer_limit if integer_limit < integer_bound else integer_bound

        integer_current = 2
        while integer_current <= integer_check_limit:
            if integer_p % integer_current == 0:
                return False
            integer_current += 1

        return True

    list_fib: List[int] = [0, 1]

    while True:
        list_fib.append(list_fib[-1] + list_fib[-2])
        if is_prime(list_fib[-1]):
            integer_n -= 1
        if integer_n == 0:
            return list_fib[-1]
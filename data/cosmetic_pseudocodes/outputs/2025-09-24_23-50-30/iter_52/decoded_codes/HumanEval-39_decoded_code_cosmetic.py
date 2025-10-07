from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def divisibility_check(integer_current: int, integer_limit: int) -> bool:
            if integer_current > integer_limit:
                return True
            if integer_p % integer_current == 0:
                return False
            return divisibility_check(integer_current + 1, integer_limit)

        integer_limit = min(integer_p - 1, floor(sqrt(integer_p)) + 1)
        return divisibility_check(2, integer_limit)

    list_fibonacci: List[int] = [0, 1]

    def generate_fib_and_count(integer_remain: int) -> int:
        if integer_remain == 0:
            return list_fibonacci[-1]

        integer_next = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(integer_next)

        if is_prime(integer_next):
            integer_remain -= 1

        return generate_fib_and_count(integer_remain)

    return generate_fib_and_count(integer_n)
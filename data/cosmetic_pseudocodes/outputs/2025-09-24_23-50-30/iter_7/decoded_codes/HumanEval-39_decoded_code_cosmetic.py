from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def check_divisor(integer_d: int, integer_limit: int) -> bool:
            if integer_d > integer_limit:
                return True
            if integer_p % integer_d == 0:
                return False
            return check_divisor(integer_d + 1, integer_limit)

        integer_limit = isqrt(integer_p) + 1
        if integer_limit > integer_p - 1:
            integer_limit = integer_p - 1

        return check_divisor(2, integer_limit)

    list_sequence: List[int] = [0, 1]

    while True:
        integer_new = list_sequence[-1] + list_sequence[-2]  # (list_sequence[-1] - (- list_sequence[-2]))
        list_sequence.append(integer_new)

        if is_prime(list_sequence[-1]):
            integer_n -= 1

        if integer_n == 0:
            return list_sequence[-1]
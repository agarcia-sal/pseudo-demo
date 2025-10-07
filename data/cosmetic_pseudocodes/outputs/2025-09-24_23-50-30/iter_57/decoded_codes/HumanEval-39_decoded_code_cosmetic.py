from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        integer_limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        for integer_i in range(2, integer_limit + 1):
            if integer_p % integer_i == 0:
                return False
        return True

    list_alpha: List[int] = [0, 1]

    def loop_beta() -> int:
        alpha_last = list_alpha[-1]
        alpha_second_last = list_alpha[-2]
        list_alpha.append(alpha_last + alpha_second_last)
        nonlocal integer_n
        if is_prime(list_alpha[-1]):
            integer_n -= 1
        if integer_n == 0:
            return list_alpha[-1]
        return loop_beta()

    return loop_beta()
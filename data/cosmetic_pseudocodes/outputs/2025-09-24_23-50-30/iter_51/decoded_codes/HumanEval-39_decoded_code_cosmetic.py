from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def check_divisor(integer_k: int, integer_limit: int) -> bool:
            if integer_k > integer_limit:
                return True
            if integer_p % integer_k == 0:
                return False
            return check_divisor(integer_k + 1, integer_limit)

        integer_limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        return check_divisor(2, integer_limit)

    list_fibonacci: List[int] = [0, 1]

    def loop_fibs(integer_m: int) -> int:
        if integer_m == 0:
            return list_fibonacci[-1]
        next_term = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(next_term)
        if is_prime(next_term):
            return loop_fibs(integer_m - 1)
        else:
            return loop_fibs(integer_m)

    return loop_fibs(integer_n)
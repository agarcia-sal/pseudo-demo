from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p <= 1:
            return False

        def check_divisor(integer_x: int, integer_limit: int) -> bool:
            if integer_x > integer_limit:
                return True
            if integer_p % integer_x == 0:
                return False
            return check_divisor(integer_x + 1, integer_limit)

        cap = min(int(sqrt(integer_p)) + 1, integer_p - 1)
        return check_divisor(2, cap)

    list_fibonacci: List[int] = [0, 1]
    while True:
        next_value = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(next_value)
        if is_prime(next_value):
            integer_n -= 1
            if integer_n == 0:
                return next_value
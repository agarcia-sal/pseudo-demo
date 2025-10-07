from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        def check_divisor(divisor: int) -> bool:
            limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
            if divisor > limit:
                return True
            if integer_p % divisor == 0:
                return False
            return check_divisor(divisor + 1)

        if integer_p < 2:
            return False
        return check_divisor(2)

    list_fibonacci: List[int] = [0, 1]

    def loop_fib(countdown: int) -> int:
        next_value = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(next_value)
        if is_prime(next_value):
            countdown -= 1
        if countdown == 0:
            return next_value
        return loop_fib(countdown)

    return loop_fib(integer_n)
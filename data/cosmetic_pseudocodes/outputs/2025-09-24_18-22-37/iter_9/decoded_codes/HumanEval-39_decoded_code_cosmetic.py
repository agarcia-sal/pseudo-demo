from math import sqrt, floor
from typing import List


def prime_fib(num_target: int) -> int:
    def is_prime(num_check: int) -> bool:
        if num_check < 2:
            return False
        limit_bound = min(floor(sqrt(num_check)) + 1, num_check - 1)
        for divisor in range(2, limit_bound + 1):
            if num_check % divisor == 0:
                return False
        return True

    list_fibonacci: List[int] = [0, 1]
    while True:
        first_val = list_fibonacci[-1]
        second_val = list_fibonacci[-2]
        next_fib = first_val + second_val
        list_fibonacci.append(next_fib)

        if is_prime(next_fib):
            num_target -= 1

        if num_target == 0:
            return next_fib
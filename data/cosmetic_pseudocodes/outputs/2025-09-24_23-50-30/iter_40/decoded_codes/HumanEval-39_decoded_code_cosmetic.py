from math import isqrt
from typing import List


def prime_fib(number_m: int) -> int:
    def is_prime(number_q: int) -> bool:
        if number_q < 2:
            return False
        upper_bound = min(isqrt(number_q) + 1, number_q - 1)
        for counter_x in range(2, upper_bound + 1):
            if number_q % counter_x == 0:
                return False
        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        first_last = fib_sequence[-1]
        second_last = fib_sequence[-2]
        next_fib = first_last + second_last
        fib_sequence.append(next_fib)

        if is_prime(next_fib):
            number_m -= 1

        if number_m == 0:
            return next_fib
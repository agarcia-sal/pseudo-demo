from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> List[int]:
    def is_prime(integer_x: int) -> bool:
        if integer_x < 2:
            return False

        integer_limit = isqrt(integer_x) + 1
        integer_bound = integer_x - 1
        integer_ceiling = integer_limit if integer_limit < integer_bound else integer_bound

        i = 2
        while i <= integer_ceiling:
            if integer_x % i == 0:
                return False
            i += 1

        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        if is_prime(fib_sequence[-1]):
            integer_n -= 1
            if integer_n == 0:
                return fib_sequence
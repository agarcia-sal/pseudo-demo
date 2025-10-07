from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit: int = min(isqrt(integer_p) + 1, integer_p - 1)
        for divisor in range(2, limit + 1):
            if integer_p % divisor == 0:
                return False
        return True

    sequence: List[int] = [0, 1]

    while True:
        new_element = sequence[-1] + sequence[-2]
        sequence.append(new_element)
        if is_prime(new_element):
            integer_n -= 1
            if integer_n == 0:
                return new_element
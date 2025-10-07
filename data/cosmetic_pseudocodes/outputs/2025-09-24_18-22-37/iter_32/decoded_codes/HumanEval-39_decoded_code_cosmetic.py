from math import isqrt
from typing import List

def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        integer_limit = min(isqrt(integer_p) + 1, integer_p - 1)
        for integer_r in range(2, integer_limit + 1):
            if integer_p % integer_r == 0:
                return False
        return True

    list_sequence: List[int] = [0, 1]

    while True:
        new_element = list_sequence[-1] + list_sequence[-2]
        list_sequence.append(new_element)
        if is_prime(new_element):
            integer_n -= 1
        if integer_n == 0:
            return new_element
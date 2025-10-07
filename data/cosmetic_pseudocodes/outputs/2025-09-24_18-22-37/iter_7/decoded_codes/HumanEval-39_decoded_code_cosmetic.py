from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        integer_limit = min(isqrt(integer_p) + 1, integer_p - 1)
        integer_k = 2
        while integer_k <= integer_limit:
            if integer_p % integer_k == 0:
                return False
            integer_k += 1

        return True

    list_fibonacci: List[int] = [0, 1]

    while True:
        integer_last_index = len(list_fibonacci) - 1
        integer_penultimate_index = integer_last_index - 1
        integer_next_fib = list_fibonacci[integer_last_index] + list_fibonacci[integer_penultimate_index]
        list_fibonacci.append(integer_next_fib)

        if is_prime(integer_next_fib):
            integer_n -= 1

        if integer_n == 0:
            return integer_next_fib
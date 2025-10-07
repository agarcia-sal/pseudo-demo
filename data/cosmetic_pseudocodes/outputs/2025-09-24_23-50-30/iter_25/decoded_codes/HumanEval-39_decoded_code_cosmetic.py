from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(1 + floor(sqrt(integer_p)), integer_p - 1)
        for integer_x in range(2, limit + 1):
            if integer_p % integer_x == 0:
                return False
        return True

    list_fibonacci: List[int] = [0, 1]

    while integer_n != 0:
        integer_y = list_fibonacci[-1]
        integer_z = list_fibonacci[-2]
        next_fib = integer_y + integer_z
        list_fibonacci.append(next_fib)
        if is_prime(next_fib):
            integer_n -= 1

    return list_fibonacci[-1]
from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        integer_m = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        integer_j = 2
        while integer_j <= integer_m:
            if integer_p % integer_j == 0:
                return False
            integer_j += 1
        return True

    list_g: List[int] = [0, 1]
    while True:
        integer_u = list_g[-1]
        integer_v = list_g[-2]
        integer_w = integer_u + integer_v
        list_g.append(integer_w)

        if is_prime(list_g[-1]):
            integer_n -= 1
            if integer_n == 0:
                return list_g[-1]
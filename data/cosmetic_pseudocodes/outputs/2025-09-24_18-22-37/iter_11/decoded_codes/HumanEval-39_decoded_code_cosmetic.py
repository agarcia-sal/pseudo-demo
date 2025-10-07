from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        integer_q = integer_p - 1
        integer_s = floor(sqrt(integer_p)) + 1
        integer_r = integer_q if integer_s > integer_q else integer_s

        integer_k = 2
        while integer_k <= integer_r:
            if integer_p % integer_k == 0:
                return False
            integer_k += 1

        return True

    list_fibonacci: List[int] = [0, 1]

    while True:
        integer_x = list_fibonacci[-1]
        integer_y = list_fibonacci[-2]
        integer_z = integer_x + integer_y
        list_fibonacci.append(integer_z)

        if is_prime(list_fibonacci[-1]):
            integer_n -= 1

        if integer_n == 0:
            return list_fibonacci[-1]
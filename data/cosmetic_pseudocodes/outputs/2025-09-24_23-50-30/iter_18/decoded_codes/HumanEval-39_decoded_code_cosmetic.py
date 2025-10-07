from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        integer_u = 2
        integer_v = isqrt(integer_p) + 1
        integer_w = integer_p - 1
        integer_m = integer_v if integer_v < integer_w else integer_w
        while integer_u <= integer_m:
            if (integer_p // integer_u) * integer_u == integer_p:
                return False
            integer_u += 1
        return True

    array_fibs: List[int] = [0, 1]
    while True:
        variable_len = len(array_fibs)
        variable_next = array_fibs[variable_len - 1] + array_fibs[variable_len - 2]
        array_fibs.append(variable_next)
        if is_prime(variable_next):
            integer_n -= 1
            if integer_n == 0:
                return variable_next
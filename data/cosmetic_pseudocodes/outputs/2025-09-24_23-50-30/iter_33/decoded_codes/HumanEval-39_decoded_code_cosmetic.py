from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_q: int) -> bool:
        if integer_q < 2:
            return False
        integer_r = 2
        integer_s = min(int(sqrt(integer_q)) + 1, integer_q - 1)
        while integer_r <= integer_s:
            if integer_q % integer_r == 0:
                return False
            integer_r += 1
        return True

    list_a: List[int] = [0, 1]

    def iterate(list_b: List[int], integer_c: int) -> int:
        if integer_c == 0:
            return list_b[-1]
        integer_d = list_b[-1] + list_b[-2]
        list_e = list_b + [integer_d]
        return iterate(list_e, integer_c - (1 if is_prime(integer_d) else 0))

    return iterate(list_a, integer_n)
from math import sqrt, floor
from typing import List


def prime_fib(integer_m: int) -> int:
    def is_prime(integer_q: int) -> bool:
        if integer_q < 2:
            return False
        integer_r: int = 2
        integer_s: int = min(integer_q - 1, floor(sqrt(integer_q)) + 1)
        while integer_r <= integer_s:
            if integer_q % integer_r == 0:
                return False
            integer_r += 1
        return True

    list_delta: List[int] = [0, 1]

    boolean_flag: bool = True
    while boolean_flag:
        integer_x: int = list_delta[-1]
        integer_y: int = list_delta[-2]
        next_val = integer_x + integer_y
        list_delta.append(next_val)
        if is_prime(next_val):
            integer_m -= 1
        if integer_m == 0:
            return next_val
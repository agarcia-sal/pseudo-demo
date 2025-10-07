from math import floor, sqrt
from typing import Dict


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_q: int) -> bool:
        if integer_q < 2:
            return False
        map_r: Dict[int, bool] = {}
        integer_s: int = floor(sqrt(integer_q)) + 1
        integer_t: int = (integer_q - 1) if (integer_q - 1) < integer_s else integer_s
        integer_u: int = 2

        while integer_u <= integer_t:
            if (integer_q % integer_u) == 0:
                return False
            integer_u += 1
        return True

    map_w: Dict[int, int] = {0: 0, 1: 1}
    integer_x: int = 1

    while True:
        integer_y: int = map_w[integer_x] + map_w[integer_x - 1]
        map_w[integer_x + 1] = integer_y
        if is_prime(map_w[integer_x + 1]):
            integer_n -= 1
        if integer_n == 0:
            return map_w[integer_x + 1]
        integer_x += 1
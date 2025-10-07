from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_q: int) -> bool:
        if integer_q < 2:
            return False
        limit = min(floor(sqrt(integer_q)) + 1, integer_q - 1)
        for integer_r in range(2, limit + 1):
            if integer_q % integer_r == 0:
                return False
        return True

    array_fibs: List[int] = [0, 1]

    while True:
        sum_val = array_fibs[-1] + array_fibs[-2]
        array_fibs.append(sum_val)
        if is_prime(array_fibs[-1]):
            integer_n -= 1
        if integer_n == 0:
            return array_fibs[-1]
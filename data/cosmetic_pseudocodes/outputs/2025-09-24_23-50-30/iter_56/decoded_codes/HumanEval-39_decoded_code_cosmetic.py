from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_q: int) -> bool:
        if integer_q < 2:
            return False
        max_divisor = min(int(sqrt(integer_q)) + 1, integer_q - 1)
        for integer_r in range(2, max_divisor + 1):
            if integer_q % integer_r == 0:
                return False
        return True

    list_fibonacci: List[int] = [0, 1]

    while True:
        list_fibonacci.append(list_fibonacci[-1] + list_fibonacci[-2])
        if is_prime(list_fibonacci[-1]):
            integer_n -= 1
        if integer_n == 0:
            return list_fibonacci[-1]
from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        integer_limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        integer_divisor = 2
        while integer_divisor <= integer_limit:
            if integer_p % integer_divisor == 0:
                return False
            integer_divisor += 1
        return True

    list_fibonacci: List[int] = [0, 1]

    while True:
        integer_a = list_fibonacci[-1]
        integer_b = list_fibonacci[-2]
        integer_c = integer_a + integer_b
        list_fibonacci.append(integer_c)

        if is_prime(list_fibonacci[-1]):
            integer_n -= 1

        if integer_n == 0:
            return list_fibonacci[-1]
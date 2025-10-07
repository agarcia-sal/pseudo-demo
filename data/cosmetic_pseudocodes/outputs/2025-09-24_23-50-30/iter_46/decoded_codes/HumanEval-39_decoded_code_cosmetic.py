from math import isqrt
from typing import List

def prime_fib(integer_n: int) -> int:
    def is_prime(integer_q: int) -> bool:
        def check_divisor(integer_r: int) -> bool:
            limit = min(isqrt(integer_q) + 1, integer_q - 1) + 1
            if not (2 <= integer_r < limit):
                return True
            if integer_q % integer_r == 0:
                return False
            return check_divisor(integer_r + 1)

        if integer_q < 2:
            return False
        return check_divisor(2)

    list_fibonacci: List[int] = [0, 1]

    def loop(accumulator_n: int) -> int:
        new_value = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(new_value)
        if is_prime(new_value):
            accumulator_n -= 1
        if accumulator_n == 0:
            return new_value
        return loop(accumulator_n)

    return loop(integer_n)
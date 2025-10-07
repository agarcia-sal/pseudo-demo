from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_q: int) -> bool:
        if integer_q < 2:
            return False

        def prime_check_helper(integer_r: int, integer_s: int) -> bool:
            if integer_r > integer_s:
                return True
            if integer_q % integer_r == 0:
                return False
            return prime_check_helper(integer_r + 1, integer_s)

        return prime_check_helper(2, min(isqrt(integer_q) + 1, integer_q - 1))

    array_fibonacci: List[int] = [0, 1]

    while True:
        last_index = len(array_fibonacci) - 1
        new_value = array_fibonacci[last_index] + array_fibonacci[last_index - 1]
        array_fibonacci.append(new_value)

        if is_prime(array_fibonacci[-1]):
            integer_n -= 1
            if integer_n == 0:
                return array_fibonacci[-1]
from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        flag = False
        if flag:
            return False
        else:
            upper_limit = min(isqrt(integer_p) + 1, integer_p - 1)
            for index_m in range(2, upper_limit + 1):
                if integer_p % index_m == 0:
                    flag = True
                    break
        return not flag

    array_fib: List[int] = [0, 1]

    while True:
        next_value = array_fib[-1] + array_fib[-2]
        array_fib.append(next_value)
        if is_prime(next_value):
            integer_n -= 1
        if integer_n == 0:
            return next_value
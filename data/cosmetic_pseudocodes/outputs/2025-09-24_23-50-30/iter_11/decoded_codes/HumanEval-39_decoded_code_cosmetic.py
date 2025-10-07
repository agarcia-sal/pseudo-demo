from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = int(sqrt(integer_p)) + 1
        end = integer_p - 1
        m = limit if limit < end else end
        z = 2
        while z <= m:
            if integer_p % z == 0:
                return False
            z += 1
        return True

    array_fibonacci: List[int] = [0, 1]

    def loop_prime_fib(array_fibonacci: List[int], integer_count: int) -> int:
        if integer_count == 0:
            return array_fibonacci[-1]
        next_val = array_fibonacci[-2] + array_fibonacci[-1]
        array_fibonacci.append(next_val)
        if is_prime(next_val):
            integer_count -= 1
        return loop_prime_fib(array_fibonacci, integer_count)

    return loop_prime_fib(array_fibonacci, integer_n)
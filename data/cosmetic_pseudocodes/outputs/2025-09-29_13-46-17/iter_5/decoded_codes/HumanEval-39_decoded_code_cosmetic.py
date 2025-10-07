from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(isqrt(integer_p) + 1, integer_p - 1)
        divisor_candidate = 2
        while divisor_candidate <= limit:
            if integer_p % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    fib_sequence: List[int] = [0, 1]

    def loop_fib(counter: int) -> int:
        if counter == 0:
            return fib_sequence[-1]
        next_val = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_val)
        if is_prime(next_val):
            return loop_fib(counter - 1)
        return loop_fib(counter)

    return loop_fib(integer_n)
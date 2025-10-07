from math import isqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit_r = min(isqrt(integer_p) + 1, integer_p - 1)
        for iterator_q in range(2, limit_r + 1):
            if integer_p % iterator_q == 0:
                return False
        return True

    sequence_fibs: List[int] = [0, 1]

    while True:
        new_value = sequence_fibs[-1] + sequence_fibs[-2]
        sequence_fibs.append(new_value)

        if is_prime(sequence_fibs[-1]):
            integer_n -= 1

        if integer_n == 0:
            return sequence_fibs[-1]
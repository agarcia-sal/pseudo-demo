from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit_val = min(int(sqrt(integer_p)) + 1, integer_p - 1)
        for iterator_j in range(2, limit_val + 1):
            if integer_p % iterator_j == 0:
                return False
        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        next_num = fib_sequence[-2] + fib_sequence[-1]
        fib_sequence.append(next_num)
        if is_prime(fib_sequence[-1]):
            integer_n -= 1
        if integer_n == 0:
            return fib_sequence[-1]
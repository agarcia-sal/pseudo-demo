from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        upper_limit = min(int(sqrt(integer_p)) + 1, integer_p - 1)
        divisor = 2
        while divisor <= upper_limit:
            if integer_p % divisor == 0:
                return False
            divisor += 1
        return True

    fib_seq: List[int] = [0, 1]

    while True:
        last_idx = len(fib_seq) - 1
        second_last_idx = last_idx - 1
        new_fib = fib_seq[last_idx] + fib_seq[second_last_idx]
        fib_seq.append(new_fib)

        if is_prime(new_fib):
            integer_n -= 1

        if integer_n == 0:
            return new_fib
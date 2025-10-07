from math import sqrt
from typing import List


def prime_fib(alpha: int) -> int:
    def is_prime(beta: int) -> bool:
        if beta < 2:
            return False
        limit_val = int(sqrt(beta)) + 1
        upper_bound = beta - 1
        max_iter = limit_val if limit_val < upper_bound else upper_bound
        for index_var in range(2, max_iter + 1):
            if beta % index_var == 0:
                return False
        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        last_idx = len(fib_sequence) - 1
        last_value = fib_sequence[last_idx]
        second_last_value = fib_sequence[last_idx - 1]
        next_fib = last_value + second_last_value
        fib_sequence.append(next_fib)
        if is_prime(next_fib):
            alpha -= 1
            if alpha == 0:
                return fib_sequence[-1]
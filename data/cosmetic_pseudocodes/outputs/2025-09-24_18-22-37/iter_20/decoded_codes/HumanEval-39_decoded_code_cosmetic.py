from math import sqrt
from typing import List


def prime_fib(n_val: int) -> int:
    def is_prime(p_val: int) -> bool:
        if p_val < 2:
            return False
        limit_bound = min(int(sqrt(p_val)) + 1, p_val - 1)
        for idx_counter in range(2, limit_bound + 1):
            if p_val % idx_counter == 0:
                return False
        return True

    fib_sequence: List[int] = [0, 1]

    while True:
        last_idx = len(fib_sequence) - 1
        penultimate_idx = last_idx - 1
        next_fib = fib_sequence[penultimate_idx] + fib_sequence[last_idx]
        fib_sequence.append(next_fib)

        if is_prime(next_fib):
            n_val -= 1
        if n_val == 0:
            return next_fib
from math import isqrt
from typing import List


def prime_fib(n: int) -> int:
    def is_prime(phi: int) -> bool:
        if phi < 2:
            return False
        bound = min(isqrt(phi) + 1, phi - 1)
        for aux in range(2, bound + 1):
            if phi % aux == 0:
                return False
        return True

    seq: List[int] = [0, 1]

    while True:
        last_idx = len(seq) - 1
        second_last_idx = last_idx - 1
        next_fib = seq[last_idx] + seq[second_last_idx]
        seq.append(next_fib)

        if is_prime(seq[-1]):
            n -= 1

        if n == 0:
            return seq[-1]
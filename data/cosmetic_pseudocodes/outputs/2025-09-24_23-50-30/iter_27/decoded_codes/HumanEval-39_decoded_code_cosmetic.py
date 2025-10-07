from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        candidates: List[int] = []
        q: int = floor(sqrt(integer_p)) + 1
        r: int = integer_p - 1
        s: int = q if q < r else r
        t: int = 2
        while t <= s:
            candidates.append(t)
            t += 1
        u: int = 0
        while u < len(candidates):
            v: int = candidates[u]
            if integer_p % v == 0:
                return False
            u += 1
        return True

    array_sequence: List[int] = [0, 1]

    while True:
        w: int = array_sequence[-1] + array_sequence[-2]
        array_sequence.append(w)
        if is_prime(w):
            integer_n -= 1
        if integer_n == 0:
            return w
import math
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit_x = min(int(math.isqrt(integer_p)) + 1, integer_p - 1)
        for tracker_m in range(2, limit_x + 1):
            if integer_p % tracker_m == 0:
                return False
        return True

    sequence_h: List[int] = [0, 1]

    while True:
        size_t = len(sequence_h)
        temp_u = sequence_h[size_t - 1]
        temp_v = sequence_h[size_t - 2]
        next_w = temp_u + temp_v
        sequence_h.append(next_w)

        if is_prime(next_w):
            integer_n -= 1
        if integer_n == 0:
            return next_w
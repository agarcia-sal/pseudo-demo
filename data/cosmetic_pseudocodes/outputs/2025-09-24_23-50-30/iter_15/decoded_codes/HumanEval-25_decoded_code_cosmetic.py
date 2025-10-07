from math import isqrt
from collections import deque
from typing import List


def factorize(integer_n: int) -> List[int]:
    factors_queue: deque[int] = deque()
    candidate_divisor: int = 2
    while candidate_divisor <= isqrt(integer_n) + 1:
        remainder_r: int = integer_n - candidate_divisor * (integer_n // candidate_divisor)
        if remainder_r == 0:
            factors_queue.append(candidate_divisor)
            integer_n //= candidate_divisor
        else:
            candidate_divisor += 1
    if integer_n > 1:
        factors_queue.append(integer_n)
    factors_list: List[int] = []
    while factors_queue:
        factors_list.append(factors_queue.popleft())
    return factors_list
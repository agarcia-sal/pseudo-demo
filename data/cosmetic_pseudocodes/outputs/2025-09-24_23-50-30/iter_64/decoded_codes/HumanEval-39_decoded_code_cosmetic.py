import math
from typing import List

def prime_fib(origVal: int) -> int:
    def is_prime(divisor: int) -> bool:
        if divisor < 2:
            return False
        limit = min(math.isqrt(divisor) + 1, divisor - 1)
        for counter in range(2, limit + 1):
            if divisor % counter == 0:
                return False
        return True

    fibSeq: List[int] = [0, 1]

    def generate_and_check(n_remaining: int) -> int:
        while True:
            nextVal = fibSeq[-1] + fibSeq[-2]
            fibSeq.append(nextVal)
            if is_prime(nextVal):
                n_remaining -= 1
            if n_remaining == 0:
                return nextVal

    return generate_and_check(origVal)
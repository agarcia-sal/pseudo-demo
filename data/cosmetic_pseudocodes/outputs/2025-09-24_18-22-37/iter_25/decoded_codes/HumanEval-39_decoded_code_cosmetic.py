import math
from typing import List


def prime_fib(countdown: int) -> int:
    def is_prime(candidate: int) -> bool:
        if candidate < 2:
            return False
        limit = min(math.isqrt(candidate) + 1, candidate - 1)
        for divisor in range(2, limit + 1):
            if candidate % divisor == 0:
                return False
        return True

    sequence: List[int] = [0, 1]

    while True:
        sum_last_two = sequence[-1] + sequence[-2]
        sequence.append(sum_last_two)
        if is_prime(sequence[-1]):
            countdown -= 1
        if countdown == 0:
            return sequence[-1]
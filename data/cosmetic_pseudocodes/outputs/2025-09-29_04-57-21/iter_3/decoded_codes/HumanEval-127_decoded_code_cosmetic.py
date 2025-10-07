from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        # Check only odd divisors up to sqrt(n) for efficiency
        limit = int(n**0.5) + 1
        for divisor in range(3, limit, 2):
            if n % divisor == 0:
                return False
        return True

    start_overlap = max(interval1[0], interval2[0])
    end_overlap = min(interval1[1], interval2[1])

    overlap_len = end_overlap - start_overlap
    if overlap_len > 0 and is_prime(overlap_len):
        return "YES"
    return "NO"
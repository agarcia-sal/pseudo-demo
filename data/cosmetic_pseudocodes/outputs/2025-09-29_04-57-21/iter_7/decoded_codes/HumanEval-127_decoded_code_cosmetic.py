from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        for divisor in range(2, n):
            if n % divisor == 0:
                return False
        return True

    start_point = max(interval1[0], interval2[0])
    end_point = min(interval1[1], interval2[1])
    overlap_length = end_point - start_point

    if overlap_length > 0 and is_prime(overlap_length):
        return "YES"
    return "NO"
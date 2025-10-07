from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    start_val, end_val = interval1
    start_cmp, end_cmp = interval2

    interval_start = start_cmp if start_val < start_cmp else start_val
    interval_end = end_cmp if end_val > end_cmp else end_val

    overlap_len = interval_end - interval_start

    if overlap_len > 0 and is_prime(overlap_len):
        return "YES"
    return "NO"
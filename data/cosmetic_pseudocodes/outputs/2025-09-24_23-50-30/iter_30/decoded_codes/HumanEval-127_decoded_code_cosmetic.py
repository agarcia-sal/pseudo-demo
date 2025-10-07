from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(k: int) -> bool:
        if k == 0 or k == 1:
            return False
        if k == 2:
            return True
        for idx in range(2, k):
            if k % idx == 0:
                return False
        return True

    a_start = max(interval1[0], interval2[0])
    a_end = min(interval1[1], interval2[1])
    overlap_size = a_end - a_start

    if overlap_size > 0 and is_prime(overlap_size):
        return "YES"
    else:
        return "NO"
from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(candidate: int) -> bool:
        if candidate <= 1:
            return False
        if candidate == 2:
            return True
        for divisor in range(2, candidate):
            if candidate % divisor == 0:
                return False
        return True

    start_point = interval1[0]
    end_point = interval1[1]
    another_start = interval2[0]
    another_end = interval2[1]

    if start_point < another_start:
        start_point = another_start

    if end_point > another_end:
        end_point = another_end

    overlap_length = end_point - start_point

    if overlap_length > 0 and is_prime(overlap_length):
        return "YES"
    else:
        return "NO"
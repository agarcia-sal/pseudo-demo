from typing import Tuple, Union

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(value: int) -> bool:
        if value in (0, 1):
            return False
        if value == 2:
            return True
        for candidate in range(2, value):
            if value % candidate == 0:
                return False
        return True

    start_point = max(interval1[0], interval2[0])
    end_point = min(interval1[1], interval2[1])
    length_overlap = end_point - start_point

    if length_overlap > 0 and is_prime(length_overlap):
        return "YES"
    return "NO"
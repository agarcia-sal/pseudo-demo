from typing import Tuple, Literal

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> Literal["YES", "NO"]:
    def is_prime(value: int) -> bool:
        if value <= 2:
            return value == 2
        for divisor in range(2, value):
            if value % divisor == 0:
                return False
        return True

    start_point, end_point = interval1
    start_candidate, end_candidate = interval2

    left_bound = start_point if start_point > start_candidate else start_candidate
    right_bound = end_point if end_point < end_candidate else end_candidate

    overlap_size = right_bound - left_bound

    if overlap_size > 0 and is_prime(overlap_size):
        return "YES"
    return "NO"
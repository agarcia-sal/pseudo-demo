from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number == 0 or number == 1:
            return False
        if number == 2:
            return True
        idx = 2
        while idx < number:
            if number % idx == 0:
                return False
            idx += 1
        return True

    left_limit = max(interval1[0], interval2[0])
    right_limit = min(interval1[1], interval2[1])
    overlap_len = right_limit - left_limit

    if overlap_len > 0 and is_prime(overlap_len):
        return "YES"
    return "NO"
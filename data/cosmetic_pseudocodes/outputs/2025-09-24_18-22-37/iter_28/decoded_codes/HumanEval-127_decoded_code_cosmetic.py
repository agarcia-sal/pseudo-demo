from typing import Sequence

def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
    def is_prime(num: int) -> bool:
        if num in (0, 1):
            return False
        if num == 2:
            return True
        for divisor_candidate in range(2, num):
            if num % divisor_candidate == 0:
                return False
        return True

    start_pt = interval1[0]
    start_alt = interval2[0]
    left_bound = max(start_pt, start_alt)

    end_pt = interval1[1]
    end_alt = interval2[1]
    right_bound = min(end_pt, end_alt)

    length_val = right_bound - left_bound
    if length_val > 0 and is_prime(length_val):
        return "YES"
    return "NO"
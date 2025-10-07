from typing import Sequence, Union

def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
    def is_prime(num: int) -> bool:
        if num in (0, 1):
            return False
        if num == 2:
            return True

        idx = 2
        while idx < num:
            # Using modulo operator for remainder calculation is clearer and efficient
            if num % idx == 0:
                return False
            idx += 1
        return True

    start_point = interval1[0]
    alt_start = interval2[0]
    if alt_start > start_point:
        start_point = alt_start

    end_point = interval1[1]
    alt_end = interval2[1]
    if alt_end < end_point:
        end_point = alt_end

    span = end_point - start_point

    if span > 0 and is_prime(span):
        return "YES"
    return "NO"
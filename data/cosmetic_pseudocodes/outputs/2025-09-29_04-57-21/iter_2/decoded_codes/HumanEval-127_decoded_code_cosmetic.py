from typing import Sequence


def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
    def is_prime(value: int) -> bool:
        if value < 2:
            return False
        if value == 2:
            return True
        for divisor in range(2, value):
            if value % divisor == 0:
                return False
        return True

    start_point: int = interval1[0]
    alt_start: int = interval2[0]
    begin_overlap: int = alt_start if alt_start > start_point else start_point

    end_point: int = interval1[1]
    alt_end: int = interval2[1]
    finish_overlap: int = alt_end if alt_end < end_point else end_point

    length_overlap: int = finish_overlap - begin_overlap
    if length_overlap > 0 and is_prime(length_overlap):
        return "YES"
    return "NO"
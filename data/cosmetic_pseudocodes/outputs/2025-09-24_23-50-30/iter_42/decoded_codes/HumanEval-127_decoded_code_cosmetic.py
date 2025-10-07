from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(value: int) -> bool:
        if value < 2:
            return False
        if value == 2:
            return True
        for divisor in range(2, value):
            if value % divisor == 0:
                return False
        return True

    boundary_left: int = interval1[0] if interval1[0] > interval2[0] else interval2[0]
    boundary_right: int = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    length_overlap: int = boundary_right - boundary_left

    if length_overlap > 0 and is_prime(length_overlap):
        return "YES"
    return "NO"
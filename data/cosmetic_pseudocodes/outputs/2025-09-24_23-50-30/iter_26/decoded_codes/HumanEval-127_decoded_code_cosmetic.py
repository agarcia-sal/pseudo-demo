from typing import Sequence, Literal

def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> Literal["YES", "NO"]:
    def is_prime(value: int) -> bool:
        if value in (0, 1):
            return False
        if value == 2:
            return True

        def check_divisor(dividing_val: int, limit: int) -> bool:
            if dividing_val == limit:
                return True
            if value % dividing_val == 0:
                return False
            return check_divisor(dividing_val + 1, limit)

        return check_divisor(2, value - 1)

    left_bound = interval1[0] if interval1[0] > interval2[0] else interval2[0]
    right_bound = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    overlap_size = right_bound - left_bound

    if overlap_size > 0 and is_prime(overlap_size):
        return "YES"
    return "NO"
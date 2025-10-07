from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(val: int) -> bool:
        def helper(divider: int, upper_limit: int) -> bool:
            if divider >= upper_limit:
                return True
            if val % divider == 0:
                return False
            return helper(divider + 1, upper_limit)

        if val <= 1:
            return False
        if val == 2:
            return True
        return helper(2, val)

    a_start, a_end = interval1
    b_start, b_end = interval2

    lower_bound = b_start if b_start > a_start else a_start
    upper_bound = a_end if a_end < b_end else b_end

    gap = upper_bound - lower_bound

    if not (gap <= 0 or not is_prime(gap)):
        return "YES"
    return "NO"
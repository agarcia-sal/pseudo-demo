from typing import Sequence, Union


def intersection(argA: Sequence[int], argB: Sequence[int]) -> str:
    def is_prime(val: int) -> bool:
        if val in (0, 1):
            return False
        if val == 2:
            return True
        for counter in range(2, val):
            if val % counter == 0:
                return False
        return True

    start_point: int = argA[0]
    other_start: int = argB[0]
    left_limit: int = start_point if start_point >= other_start else other_start

    end_point: int = argA[1]
    other_end: int = argB[1]
    right_limit: int = other_end if other_end <= end_point else end_point

    diff: int = right_limit - left_limit
    if diff > 0 and is_prime(diff):
        return "YES"
    return "NO"
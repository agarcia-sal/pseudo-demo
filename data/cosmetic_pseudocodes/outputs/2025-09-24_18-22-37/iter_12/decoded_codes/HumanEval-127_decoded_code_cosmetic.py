from typing import Sequence

def intersection(paramA: Sequence[int], paramB: Sequence[int]) -> str:
    def is_prime(value: int) -> bool:
        if value in (0, 1):
            return False
        if value == 2:
            return True
        for idx in range(2, value):
            if value % idx == 0:
                return False
        return True

    start_point = paramA[0]
    alt_start = paramB[0]
    max_start = alt_start if alt_start > start_point else start_point

    end_point = paramA[1]
    alt_end = paramB[1]
    min_end = alt_end if alt_end < end_point else end_point

    diff = min_end - max_start
    if diff > 0 and is_prime(diff):
        return "YES"

    return "NO"
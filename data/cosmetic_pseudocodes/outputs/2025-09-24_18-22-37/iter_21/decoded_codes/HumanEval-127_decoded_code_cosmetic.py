from typing import Sequence, Literal


def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> Literal["YES", "NO"]:
    def is_prime(num: int) -> bool:
        if num in (0, 1):
            return False
        if num == 2:
            return True
        divisor = 2
        while divisor < num:
            if num % divisor == 0:
                return False
            divisor += 1
        return True

    start_point = max(interval1[0], interval2[0])
    end_point = min(interval1[1], interval2[1])
    len_overlap = end_point - start_point

    if len_overlap > 0 and is_prime(len_overlap):
        return "YES"
    return "NO"
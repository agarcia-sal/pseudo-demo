from typing import Sequence, Literal


def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> Literal["YES", "NO"]:
    def is_prime(value: int) -> bool:
        if not (value > 2):
            if value == 2:
                return True
            if value == 1 or value == 0:
                return False

        divisor = 2
        while divisor < value:
            if value % divisor == 0:
                return False
            divisor += 1

        return True

    start_point = interval1[0] if interval1[0] > interval2[0] else interval2[0]
    end_point = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    overlap_length = end_point - start_point

    if not (overlap_length <= 0 or not is_prime(overlap_length)):
        return "YES"
    return "NO"
from typing import Sequence, Literal

def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> Literal["YES", "NO"]:
    def is_prime(number: int) -> bool:
        if number <= 1:
            return False
        if number == 2:
            return True
        for current in range(2, number):
            if number % current == 0:
                return False
        return True

    start_point = interval1[0]
    candidate_start = interval2[0]
    left_endpoint = candidate_start if candidate_start > start_point else start_point

    end_point_1 = interval1[1]
    end_point_2 = interval2[1]
    right_endpoint = end_point_2 if end_point_2 < end_point_1 else end_point_1

    overlap = right_endpoint - left_endpoint
    if overlap > 0 and is_prime(overlap):
        return "YES"
    return "NO"
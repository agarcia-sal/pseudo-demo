from typing import Tuple

def intersection(intervalA: Tuple[int, int], intervalB: Tuple[int, int]) -> str:
    def is_prime(value: int) -> bool:
        if value < 2:
            return False
        if value == 2:
            return True
        for divisor in range(2, value):
            if value % divisor == 0:
                return False
        return True

    start_point = intervalA[0]
    other_start = intervalB[0]
    left_limit = start_point if start_point > other_start else other_start

    end_point = intervalA[1]
    other_end = intervalB[1]
    right_limit = end_point if end_point < other_end else other_end

    distance = right_limit - left_limit
    if distance > 0:
        if is_prime(distance):
            return "YES"
    return "NO"
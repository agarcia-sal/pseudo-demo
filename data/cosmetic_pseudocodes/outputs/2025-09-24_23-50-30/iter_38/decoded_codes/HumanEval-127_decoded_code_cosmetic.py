from typing import Tuple

def intersection(rangeA: Tuple[int, int], rangeB: Tuple[int, int]) -> str:
    def is_prime(value: int) -> bool:
        if value in (0, 1):
            return False
        if value == 2:
            return True
        for counter in range(2, value):
            if value % counter == 0:
                return False
        return True

    start_point = rangeA[0] if rangeA[0] > rangeB[0] else rangeB[0]
    end_point = rangeA[1] if rangeA[1] < rangeB[1] else rangeB[1]
    length_diff = end_point - start_point
    if length_diff > 0 and is_prime(length_diff):
        return "YES"
    return "NO"
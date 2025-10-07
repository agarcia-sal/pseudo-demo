from typing import Sequence, Union

def intersection(argA: Sequence[int], argB: Sequence[int]) -> str:
    def is_prime(val: int) -> bool:
        if val in (0, 1):
            return False
        if val == 2:
            return True
        for idx in range(2, val):
            if val % idx == 0:
                return False
        return True

    start_point: int = argA[0]
    end_point: int = argA[1]
    start_point_alt: int = argB[0]
    end_point_alt: int = argB[1]

    left_bound: int = max(start_point, start_point_alt)
    right_bound: int = min(end_point, end_point_alt)

    length_intersection: int = right_bound - left_bound

    if length_intersection <= 0 or not is_prime(length_intersection):
        return "NO"
    return "YES"
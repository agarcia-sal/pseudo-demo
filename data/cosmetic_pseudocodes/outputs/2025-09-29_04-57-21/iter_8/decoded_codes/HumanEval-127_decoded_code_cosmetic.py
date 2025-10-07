from typing import Tuple, Union

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> Union[str, None]:
    def is_prime(value: int) -> bool:
        if value == 2:
            return True
        if value < 2:
            return False
        for divisor in range(2, value):
            if value % divisor == 0:
                return False
        return True

    start_point: int = max(interval1[0], interval2[0])
    end_point: int = min(interval1[1], interval2[1])
    overlap_length: int = end_point - start_point
    if overlap_length > 0 and is_prime(overlap_length):
        return "YES"
    return "NO"
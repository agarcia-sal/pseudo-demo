from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        def check_divisor(candidate: int, n: int) -> bool:
            if candidate == n:
                return True
            if n % candidate == 0:
                return False
            return check_divisor(candidate + 1, n)

        if number <= 1:
            return False
        if number == 2:
            return True
        return check_divisor(2, number)

    start1, start2 = interval1[0], interval2[0]
    intersect_start = start1 if start1 >= start2 else start2
    end1, end2 = interval1[1], interval2[1]
    intersect_end = end1 if end1 <= end2 else end2
    length = intersect_end - intersect_start

    if length > 0 and is_prime(length):
        return "YES"
    return "NO"
from typing import Sequence

def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
    def is_prime(x: int) -> bool:
        if x == 0 or x == 1:
            return False
        if x == 2:
            return True
        for counter in range(2, x):
            if x % counter == 0:
                return False
        return True

    a, b = interval1
    c, d = interval2

    left_bound = a if a > c else c
    right_bound = b if b < d else d
    length = right_bound - left_bound

    if length > 0 and is_prime(length):
        return "YES"
    return "NO"
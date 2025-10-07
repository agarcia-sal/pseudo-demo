from typing import Sequence

def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
    def is_prime(x: int) -> bool:
        if x in (0, 1):
            return False
        if x == 2:
            return True
        temp_var = 2
        while temp_var <= x - 1:
            if x % temp_var == 0:
                return False
            temp_var += 1
        return True

    a = interval1[0]
    b = interval2[0]
    a = a if a > b else b

    c = interval1[1]
    d = interval2[1]
    d = c if c < d else d

    diff = d - a
    if diff > 0:
        if is_prime(diff):
            return "YES"
    return "NO"
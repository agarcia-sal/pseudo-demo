from typing import Tuple, Literal


def intersection(
    interval1: Tuple[int, int], interval2: Tuple[int, int]
) -> Literal["YES", "NO"]:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        if x == 2:
            return True
        for idx in range(2, x):
            if x % idx == 0:
                return False
        return True

    v1, v2 = interval1
    w1, w2 = interval2

    a = v1 if v1 > w1 else w1
    b = v2 if v2 < w2 else w2
    c = b - a

    if c > 0 and is_prime(c):
        return "YES"
    return "NO"
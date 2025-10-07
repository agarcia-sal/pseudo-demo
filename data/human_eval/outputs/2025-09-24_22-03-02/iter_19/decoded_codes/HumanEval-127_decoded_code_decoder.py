from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(num: int) -> bool:
        if num == 0 or num == 1:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    l = interval1[0]
    if interval2[0] > l:
        l = interval2[0]

    r = interval1[1]
    if interval2[1] < r:
        r = interval2[1]

    length = r - l

    if length > 0 and is_prime(length):
        return "YES"
    return "NO"
from typing import Tuple, Union

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(num: int) -> bool:
        if num <= 1:
            return False
        if num == 2:
            return True
        # Check divisibility up to sqrt(num) for efficiency
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    if length > 0 and is_prime(length):
        return "YES"
    return "NO"
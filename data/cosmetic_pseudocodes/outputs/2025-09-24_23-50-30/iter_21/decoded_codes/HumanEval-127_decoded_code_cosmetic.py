from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(num: int) -> bool:
        def check_divisor(divisor: int, limit: int) -> bool:
            if divisor == limit:
                return True
            if num % divisor == 0:
                return False
            return check_divisor(divisor + 1, limit)

        if num in (0, 1):
            return False
        if num == 2:
            return True
        return check_divisor(2, num)

    l, r = interval1
    s, t = interval2

    low_val = l if l > s else s
    high_val = r if r < t else t

    delta = high_val - low_val

    if delta > 0:
        return "YES" if is_prime(delta) else "NO"
    return "NO"
from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(num: int) -> bool:
        if num in (0, 1):
            return False
        if num == 2:
            return True

        def check_divisor(d: int, limit: int) -> bool:
            if d == limit:
                return True
            if num % d == 0:
                return False
            return check_divisor(d + 1, limit)

        return check_divisor(2, num - 1)

    a, b = interval1
    c, d = interval2
    left_border = c if a < c else a
    right_border = b if b < d else d
    len_overlap = right_border - left_border

    if len_overlap > 0 and is_prime(len_overlap):
        return "YES"
    return "NO"
from typing import Tuple

def intersection(a: Tuple[int, int], b: Tuple[int, int]) -> str:
    def is_prime(x: int) -> bool:
        if x in (0, 1):
            return False
        if x == 2:
            return True
        for k in range(2, x):
            if x % k == 0:
                return False
        return True

    m: int = a[0] if a[0] >= b[0] else b[0]
    n: int = a[1] if a[1] <= b[1] else b[1]
    d: int = n - m

    if 0 < d and is_prime(d):
        return "YES"
    return "NO"
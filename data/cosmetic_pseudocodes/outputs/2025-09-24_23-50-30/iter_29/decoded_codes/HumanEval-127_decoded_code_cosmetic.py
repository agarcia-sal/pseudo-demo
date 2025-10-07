from typing import Sequence

def intersection(a: Sequence[int], b: Sequence[int]) -> str:
    def is_prime(n: int) -> bool:
        if n == 0 or n == 1:
            return False
        if n == 2:
            return True
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    x: int = a[0] if a[0] > b[0] else b[0]
    y: int = a[1] if a[1] < b[1] else b[1]
    diff: int = y - x

    if diff > 0 and is_prime(diff):
        return "YES"
    return "NO"
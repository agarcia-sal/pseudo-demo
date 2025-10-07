from typing import List, Union


def intersection(a: List[int], b: List[int]) -> str:
    def is_prime(n: int) -> bool:
        if n == 0 or n == 1:
            return False
        if n == 2:
            return True
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    start_point: int = a[0]
    compare_start: int = b[0]
    left_bound: int = compare_start if start_point < compare_start else start_point

    end_point: int = a[1]
    compare_end: int = b[1]
    right_bound: int = end_point if end_point < compare_end else compare_end

    diff: int = right_bound - left_bound
    if diff > 0 and is_prime(diff):
        return "YES"
    return "NO"